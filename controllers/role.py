import datetime
import json
import traceback
from flask import Flask, jsonify, request
from flask import Blueprint
from common.baseResponseSingle import BaseResponseSingle
from models.role import Role
from schema.roleSchema import RoleSchema
from services.roleService import RoleService
from common.baseResponse import BaseResponse
from common.errorResponse import ErrorResponse
from app import db

ts = datetime.datetime.utcnow()

role_api = Blueprint('role_api', __name__)

@role_api.route("/role", methods=["GET"])
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
        role_schema = RoleSchema(many=True)
        data = RoleService.get_list(search, page, limit, sortBy) 
        print(role_schema.dump(data))
        return jsonify(
            BaseResponse(
                role_schema.dump(data),
                "Role successfully Show",
                page,
                limit,
                len(role_schema.dump(data)),
                200,
            ).serialize()
        ), 200

    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())

@role_api.route('/role', methods=["POST"]) 
def add_role():
    json = request.json

    role = json.get('role')

    try:
        add_role = Role(
            role = role,
            created_at=ts,
            updated_at=None,
            deleted_at=None
        )
        db.session.add(add_role)
        db.session.commit()

        return (
            jsonify(
                BaseResponseSingle(
                    role,
                    "Role successfully Add",
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
    
@role_api.route('/role/<string:id>', methods=["GET"])
def get_by_id(id):
    try:
        data = RoleService.get_by_id(id) 
        if not data:
            return ErrorResponse(exception="Role is Not Found", code=400).serialize()
        role_schema = RoleSchema()
        return (
            jsonify(
                BaseResponseSingle(
                    role_schema.dump(data),
                    "Role successfully Showed",
                    200,
                ).serialize()
            ),
            200
        )
    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
    
@role_api.route('/role/<string:id>', methods=["PUT"])
def update_role(id):

    role = request.json.get('role')
    try:
        data = RoleService.get_by_id(id)
        if not data or data.deleted_at is not None:
            return ErrorResponse(exception="Role is Not Found", code=400).serialize()

        data.role = role
        data.updated_at = ts
        db.session.commit()

        role_schema = RoleSchema() 

        return (
            jsonify(
                BaseResponseSingle(
                    role_schema.dump(data), 
                    "Role successfully Updated",
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


@role_api.route('/role/delete/<string:id>', methods=["PUT"])
def delete_role(id):
    
    try:
        data = RoleService.get_by_id(id)
        if data.deleted_at is not None:
            return ErrorResponse(exception="Role is Not Found", code=400).serialize()
        
        data.deleted_at = ts
        db.session.commit()

        return (
            jsonify(
                BaseResponseSingle(
                    data.id,
                    "Role successfully Deleted",
                    200,
                ).serialize()
            ),
            200
        )
    except Exception as e:
        traceback.print_exc()
        response = BaseResponse(None, str(e), 0, 0, 0, 400)
        return jsonify(response.serialize())
