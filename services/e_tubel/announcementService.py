from models.e_tubel.announcement import Announcement
from schema.e_tubel.announcementSchema import AnnouncementSchema
from app import db
from flask import request, json
from datetime import datetime
ts = datetime.utcnow()

class AnnouncementService:
    @staticmethod
    def manual_announce(schema:AnnouncementSchema):
        announce=Announcement(
            announce_body=schema['announce_body'],
            announce_isRead=False,
            deleted_at=ts
        )
        db.session.add(announce)
        db.session.commit()
        return announce 
    
    def edit_announce(input_id):
        data=Announcement.query.filter(Announcement.announce_id==input_id).first()
        if data is not None:
            data.announce_body=request.json['announce_body']
            db.session.commit()
            return data
        else:
            return None
    
    @staticmethod
    #sementara get semua dulu
    # def get_unread(data_emp):
    def get_unread():
        filtering=Announcement.query.filter(Announcement.announce_isRead==False).group_by(Announcement.announce_id)
        
        # filtering=Announcement.query.filter(Announcement.emp_id==data_emp,
        #                                     Announcement.announce_isRead==False).group_by(Announcement.announce_id)
        
        data=[]
        for i in filtering:
            id=i.announce_id
            body=i.announce_body
            data.append({"id":id, "body":body})
        return data
    
    @staticmethod
    def get_unread_id(announce_id):
        filtering=Announcement.query.filter(Announcement.announce_id==announce_id,
                                            Announcement.announce_isRead==False).group_by(Announcement.announce_id)
        data=[]
        for i in filtering:
            id=i.announce_id
            body=i.announce_body
            data.append({"id":id, "body":body})
        return data
    
    @staticmethod
    def get_by_id(id):
        data=Announcement.query.filter(Announcement.announce_id==id).first()
        return data
        