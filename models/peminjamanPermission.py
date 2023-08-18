from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app import db

class peminjamanPermission(db.Model):
    __tablename__ = "peminjaman_Permission"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    peminjaman_id = db.Column(UUID(as_uuid=True), ForeignKey("peminjaman.id"))
    permission_id = db.Column(db.String(36), ForeignKey("permission_id"))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    peminjaman = relationship("Peminjaman", backref="peminjaman_permission")
    permission = relationship("Permission", backref="peminjaman_permission")

    def __init__(self, peminjaman_id, permission_id, created_at, updated_at, deleted_at):
        self.peminjaman_id = peminjaman_id,
        self.permission_id = permission_id,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)