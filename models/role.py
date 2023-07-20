from datetime import datetime
import uuid
from app import db

class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    role = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    def __init__(self, id, role, created_at, updated_at, deleted_at):
        self.id = id,
        self.role = role,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)
