from app import db

class Announcement(db.Model):
    __tablename__ = 'announcement'
    
    announce_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    announce_body = db.Column(db.String(), nullable=True)
    announce_isRead = db.Column(db.Boolean(), nullable=True)
    deleted_at=db.Column(db.TIMESTAMP(), nullable=True)
    
    def __init__(self,
                 announce_body, announce_isRead, deleted_at):
        self.announce_body=announce_body
        self.announce_isRead=announce_isRead
        self.deleted_at=deleted_at
        
    def repr(self):
        return '<id {}>'.format(self.announce_id)
    
    def serialize(self):
        return{
            "id" : self.announce_id,
            "body" : self.announce_body,
            "isRead"  : self.announce_isRead,
            "deleted_at" : self.deleted_at
        }