from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app import db

class peminjamanPermission(db.Model):
    __tablename__ = "peminjaman_Permission"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    nama = db.Column(db.String(36))
    judul_buku = db.Column(db.String(225))
    tanggal_peminjaman = db.Column(db.String(225))
    tanggal_pengembalian = db.column(db.String(225))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    def __init__(self, nama, judul_buku, tanggal_peminjaman, tanggal_pemgembalian, created_at, updated_at, deleted_at):
        self.nama = nama,
        self.judul_buku = judul_buku,
        self.tanggal_peminjaman = tanggal_peminjaman,
        self.tanggal_pengembalian = tanggal_pemgembalian,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)