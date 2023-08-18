from sqlalchemy import ForeignKey
from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json
import uuid

class Peminjaman(db.Model):
    __tablename__ = "peminjaman"
    id = db.Columnid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), ForeignKey('users.id'))   
    buku_id = db.Column(UUID(as_uuid=True), ForeignKey('buku.id'))   
    tanggal_peminjaman = db.Column(db.String(255))
    tanggal_pengembalian = db.Column(db.String(225))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    user = relationship("Users", backref="peminjaman")
    buku = relationship("Buku", backref="peminjaman")


     


def __init__(
        self,
        user_id,
        buku_id,
        tanggal_peminjaman,
        tanggal_pengembalian,
        deleted_at,
        created_at,
        updated_at,
    ):
        self.user_id = user_id
        self.buku_id = buku_id
        self.tanggal_peminjaman = tanggal_peminjaman
        self.tanggal_pengembalian = tanggal_pengembalian
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

def __repr__(self):
        return "<id {}>".format(self.id)

   

    