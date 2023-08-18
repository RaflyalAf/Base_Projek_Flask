import datetime
import json
import traceback
from flask import Flask, jsonify, request
from flask import Blueprint
from common.baseResponseSingle import BaseResponseSingle
from models.Buku import Buku
from schema.bukuSchema import BukuSchema
from services.bukuService import BukuService
from common.baseResponse import BaseResponse
from common.errorResponse import ErrorResponse
from app import db

ts = datetime.datetime.utcnow()

buku_api = Blueprint('buku_api', __name__)

@buku_api.route("/buku", methods=["GET"])
def get_list():

    args = request.args
    search = args.get("search", "")
    page = args.get("page", 1)
    try:
        page = int(page)
    except ValueError:
        pass
    limit = args.get("limit", 10)
    try:
        limit = int(limit)
    except ValueError:
        pass
    sortBy = args.get("sortBy", "id,desc")
        
    try:
        buku_schema = BukuSchema(many=True)
        data = BukuService.get_list(search, page, limit, sortBy) 
        print(buku_schema.dump(data))
        return jsonify(
            BaseResponse(
                buku_schema.dump(data),
                "buku berhasil di tampilkan",
                page,
                limit,
                len(buku_schema.dump(data)),
                200,
            ).serialize()
        ), 200

    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())


    
@buku_api.route('/buku/<string:id>', methods=["GET"])
def get_by_id(id):
    try:
        data = BukuService.get_by_id(id) 
        if not data:
            return ErrorResponse(exception="buku tidak ada", code=400).serialize()
        buku_schema = BukuSchema()
        return (
            jsonify(
                BaseResponseSingle(
                    buku_schema.dump(data),
                    "buku berhasil di tampilkan",
                    200,
                ).serialize()
            ),
            200
        )
    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
    
@buku_api.route('/buku/<string:id>', methods=["PUT"])
def update_buku(id):

    buku = request.json.get('kelas')
    try:
        data = BukuService.get_by_id(id)
        if not data or data.deleted_at is not None:
            return ErrorResponse(exception="buku is Not Found", code=400).serialize()

        data.buku = buku
        data.updated_at = ts
        db.session.commit()

        buku_schema = BukuSchema() 

        return (
            jsonify(
                BaseResponseSingle(
                    buku_schema.dump(data), 
                    "buku successfully Updated",
                    200,
                ).serialize()
            ),
            200
        )
    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())



@buku_api.route('/buku/delete/<string:id>', methods=["PUT"])
def delete_buku(id):
    
    try:
        data = BukuService.get_by_id(id)
        if data.deleted_at is not None:
            return ErrorResponse(exception="Buku tidak ada", code=400).serialize()
        
        data.deleted_at = ts
        db.session.commit()

        return (
            jsonify(
                BaseResponseSingle(
                    data.id,
                    "Buku berhasil di hapus",
                    200,
                ).serialize()
            ),
            200
        )
    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())

@buku_api.route('/buku', methods=["POST"]) 
# @jwt_required()
def buku():
    try:
        buku_schema = BukuSchema()
        buku = buku_schema.load(request.json)

        if not buku.get('judul_buku'):
            return ErrorResponse(exception="Judul_Buku is Required", code=400).serialize()
        if not buku.get('kategori_buku'):
            return ErrorResponse(exception="Kategori_buku is Required", code=400).serialize()
        if not buku.get('penerbit'):
            return ErrorResponse(exception="Penerbit is Required", code=400).serialize()  
        if not buku.get('pengarang'):
            return ErrorResponse(exception="Pengarang is Required", code=400).serialize()   
       
        

        add_buku = Buku(
            judul_buku=buku['judul_buku'],
            kategori_buku=buku['kategori_buku'],
            penerbit=buku["penerbit"],
            pengarang=buku["pengarang"],
            created_at=ts,
            updated_at=None,
            deleted_at=None,
            
        )

        db.session.add(add_buku)
        db.session.commit()

        data = buku_schema.dump(add_buku)
        
    
        return jsonify(
            BaseResponseSingle(
                data,
                "buku berhasil ditambahkan",
                200
            ).serialize()
        ), 200

    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
    