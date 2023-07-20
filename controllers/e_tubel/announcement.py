from flask import Blueprint, request, json, jsonify
from schema.e_tubel.announcementSchema import AnnouncementSchema
from services.e_tubel.announcementService import AnnouncementService
from common.baseResponse import BaseResponse
import traceback
from common.baseResponseSingle import BaseResponseSingle
from common.errorResponse import ErrorResponse

announcement=Blueprint('announcement', __name__)

@announcement.route('/manual-announce', methods=['POST'])
def manual_announce():
    schema=AnnouncementSchema()
    announce=schema.load(request.json)
    
    try:
        data=AnnouncementService.manual_announce(announce)
        return(
            jsonify(
                BaseResponseSingle(
                    schema.dump(data),
                    "Success",
                    200,
                ).serialize()
            ),200
        )
    except Exception as e:
        traceback.print_exc()
        response=BaseResponse(None, str(e), 0,0,0, False)
        return jsonify(response.serialize())
    
    
@announcement.route("/get-unread", methods=['GET'])
# @jwt_required()
def get_unread():
    # user_auth = get_jwt_identity()
    # username = user_auth['name']
    try:
        # emp = EmployeeService.get_employee_by_name(username).emp_id
        data=AnnouncementService.get_unread()
        print(data)
        if len(data)!=0:
            datas={"isRead" : False}
        if len(data)==0:
            datas={"isRead" : True}
        return(
            jsonify(
                BaseResponseSingle(
                    datas,
                    "success",
                    200
                ).serialize()
            ),200
        )
    except Exception as e:
        traceback.print_exc()
        response=(BaseResponseSingle(None, str(e), 400))
        return(jsonify(response.serialize()))
    
@announcement.route("/get-unread-id/<int:announce_id>", methods=['GET'])
def get_unread_id(announce_id):
    try:
        data=AnnouncementService.get_unread_id(announce_id)
        print(data)
        if len(data)!=0:
            datas={"isRead" : False}
        if len(data)==0:
            datas={"isRead" : True}
        return(
            jsonify(
                BaseResponseSingle(
                    datas,
                    "success",
                    200
                ).serialize()
            ),200
        )
    except Exception as e:
        traceback.print_exc()
        response=(BaseResponseSingle(None, str(e), 400))
        return(jsonify(response.serialize()))
    
@announcement.route("/edit-announcement/<int:announce_id>", methods=['PUT'])
def edit(announce_id):
    filtering=AnnouncementService.get_by_id(announce_id)
    if filtering is None:
        return ErrorResponse(exception="Data not Found", code=400).serialize()
    schema=AnnouncementSchema()
    try:
        data=AnnouncementService.edit_announce(announce_id)
        final=schema.dump(data)
        return(
            jsonify(
                BaseResponseSingle(
                    final,
                    "Success",
                    200,
                ).serialize()
            ),200
        )
    except Exception as e:
        traceback.print_exc()
        response=BaseResponse(None, str(e), 0,0,0, False)
        return jsonify(response.serialize())
    
    
    