from sqlalchemy import ForeignKey
from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import json
import uuid

class Peminjaman(db.Model):
    __tablename__ = "peminjaman"
    id = db.Columnid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nama = db.Column(db.String(36))
    judul_buku = db.Column(db.String(36))
    tanggal_peminjaman = db.Column(db.String(255))
    tanggal_pengembalian = db.Column(db.String(225))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)


def __init__(
        self,
        nama,
        judul_buku,
        tanggal_peminjaman,
        tanggal_pengembalian,
        deleted_at,
        created_at,
        updated_at,
    ):
        self.nama = nama
        self.judul_buku = judul_buku
        self.tanggal_peminjaman = tanggal_peminjaman
        self.tanggal_pengembalian = tanggal_pengembalian
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

def __repr__(self):
        return "<id {}>".format(self.id)

   

    