
from sqlalchemy import ForeignKey
from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime 
import json
import uuid

class Buku(db.Model):
    __tablename__ = "buku"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    judul_buku = db.Column(db.String(255))
    kategori_buku = db.Column(db.String(225))
    penerbit = db.Column(db.String(225))
    pengarang = db.Column(db.String(225))
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    def __init__(self, judul_buku, kategori_buku, penerbit, pengarang, created_at, updated_at, deleted_at):
        self.judul_buku = judul_buku,
        self.kategori_buku = kategori_buku,
        self.penerbit = penerbit,
        self.pengarang = pengarang,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)

   

    