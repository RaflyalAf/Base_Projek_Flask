from datetime import datetime
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app import db

class RolePermission(db.Model):
    __tablename__ = "role_permission"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    role_id = db.Column(db.String(36), ForeignKey('role.id'))
    permission_id = db.Column(db.String(36), ForeignKey('permission.id'))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    role = relationship("Role", backref="role_permission")
    permission = relationship("Permission", backref="role_permission")

    def __init__(self, role_id, permission_id, created_at, updated_at, deleted_at):
        self.role_id = role_id,
        self.permission_id = permission_id,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)
