from flask import Blueprint, json, request, jsonify
from schema.e_tubel.emailNotifSchema import EmailNotificationSchema
from services.e_tubel.emailNotification import EmailNotificationService
from common.baseResponse import BaseResponse
from common.errorResponse import ErrorResponse 
import traceback

email_notif=Blueprint('email_notif', __name__)

@email_notif.route('/usual_send', methods=['POST'])
def usual_send():
    schema=EmailNotificationSchema()
    notif=schema.load(request.json)
    try:
        data=EmailNotificationService.manual_send(notif)
        return (
            jsonify(
                BaseResponse(
                    schema.dump(data),
                    "Success",
                    1,1,1,True,
                ).serialize()
            ),200            
        )
    except Exception as e:
        traceback.print_exc()
        response=BaseResponse(None, str(e), 0,0,0, False)
        return jsonify(response.serialize())
    
@email_notif.route("/send_to_email", methods=['POST'])
def send_to_email():
    sender_email = 't489045@gmail.com'
    receiver_emails = 'nurditha5@gmail.com'
    subject = 'test'
    password = 'tesT-123'
    body = 'test'
    
    try:
        data=EmailNotificationService.send_to_email(sender_email, receiver_emails, subject, body, password)
        print(data)
        return (
            jsonify(
                BaseResponse(
                    "success",
                    "Success",
                    1,1,1,True,
                ).serialize()
            ),200            
        )
        
    except Exception as e:
        traceback.print_exc()
        response=BaseResponse(None, str(e), 0,0,0, False)
        return jsonify(response.serialize())