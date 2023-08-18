import datetime
import traceback
import validators
from flask import Flask, jsonify, request
from flask import Blueprint
from common.baseResponse import BaseResponse
from common.baseResponseSingle import BaseResponseSingle
from common.errorResponse import ErrorResponse
from models.peminjaman import Peminjaman
from schema.peminjamanSchema import peminjamanSchema
from schema.userSchema import UserSchema
from app import db
from services.logActivityService import LogActivityService
from services.peminjamanService import peminjamanService
from services.bukuService import BukuService
from services.userService import UserService
from services.peminjamanService import peminjamanService
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token, create_refresh_token

ts = datetime.datetime.utcnow()

peminjaman_api = Blueprint('peminjaman_api', __name__)

@peminjaman_api.route("/peminjaman", methods=["GET"])
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
        peminjaman_schema = peminjamanSchema(many=True)
        data = peminjamanService.get_list(search, page, limit, sortBy) 
        print(peminjaman_schema.dump(data))
        return jsonify(
            BaseResponse(
                peminjaman_schema.dump(data),
                "Peminjaman successfully Show",
                page,
                limit,
                len(peminjaman_schema.dump(data)),
                200,
            ).serialize()
        ), 200

    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
    
@peminjaman_api.route('/peminjaman/<string:id>', methods=["GET"])
def get_by_id(id):
    try:
        data = peminjamanService.get_by_id(id) 
        if not data:
            return ErrorResponse(exception="Peminjaman is Not Found", code=400).serialize()
        peminjaman_schema = peminjamanSchema()
        return (
            jsonify(
                BaseResponseSingle(
                    peminjaman_schema.dump(data),
                    "Peminjaman successfully Showed",
                    200,
                ).serialize()
            ),
            200
        )
    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
    
@peminjaman_api.route('/peminjaman', methods=["POST"]) 
# @jwt_required()
def pembayaran():
    try:
        peminjaman_schema = peminjamanSchema()
        peminjaman = peminjaman_schema.load(request.json)

        
        if not peminjaman.get('tanggal_peminjaman'):
            return ErrorResponse(exception="Tanggal_peminjaman is Required", code=400).serialize()  
        if not peminjaman.get('tanggal_pengembalian'):
            return ErrorResponse(exception="tanggal_pengembalian is Required", code=400).serialize() 
        if not peminjaman.get('name'):
            return ErrorResponse(exception="Nama is Required", code=400).serialize() 
        if not peminjaman.get('judul_buku'):
            return ErrorResponse(exception="judul_buku is Required", code=400).serialize()    
       
        user = UserService.get_by_name(name=peminjaman.get("name"))
        buku = BukuService.get_by_judul_buku(judul_buku=peminjaman.get("judul_buku"))

        add_peminjaman = Peminjaman(
            user_id=user.id,
            buku_id=buku.id,
            tanggal_peminjaman = peminjaman['tanggal_peminjaman'],
            tanggal_pengembalian = peminjaman['tanggal_peminjaman'],
            created_at=ts,
            updated_at=None,
            deleted_at=None,
        )

        db.session.add(add_peminjaman)
        db.session.commit()

        data = peminjaman_schema.dump(add_peminjaman)
        data["name"] = user.name # Add user name to the data dictionary
        
        return jsonify(
            BaseResponseSingle(
                data,
                "Peminjaman Successfully",
                200
            ).serialize()
        ), 200

    except Exception as e:
        traceback.print_exc()
        db.session.rollback()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
    