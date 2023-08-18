from datetime import datetime
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app import db

class BukuPermission(db.Model):
    __tablename__ = "buku_permission"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    buku_id = db.Column(db.String(36), ForeignKey('buku_id'))
    permission_id = db.Column(db.String(36), ForeignKey('permission.id'))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    buku = relationship("Buku", backref="buku_permission")
    permission = relationship("Permission", backref="buku_permission")

    def __init__(self, buku_id, permission_id, created_at, updated_at, deleted_at):
        self.buku_id = buku_id,
        self.permission_id = permission_id,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)
