from app import db
from sqlalchemy.orm import *

class EmailNotification(db.Model):
    __tablename__ = "email_notification"
    
    email_notif_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email_notif_from = db.Column(db.String(50), nullable=True)
    email_notif_to = db.Column(db.String(50), nullable=True)
    email_notif_body = db.Column(db.String(), nullable=True)
    email_notif_isRead = db.Column(db.Boolean(), nullable=True)
    
    def __init__(self,
                 email_notif_from, email_notif_to, email_notif_body, email_notif_isRead):
        self.email_notif_from = email_notif_from,
        self.email_notif_to = email_notif_to,
        self.email_notif_body = email_notif_body,
        self.email_notif_isRead = email_notif_isRead
        
    def __repr__(self):
        return "<id {}>".format(self.email_notif_id)
    
    def serialize(self):
        return {
            "id" : self.email_notif_id,
            "sender" : self.email_notif_from,
            "receiver" : self.email_notif_to,
            "body" : self.email_notif_body,
            "isRead" : self.email_notif_isRead,
        }
    