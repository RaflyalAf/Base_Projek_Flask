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
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    tanggal_peminjaman = db.Column(db.String(255))
    tanggal_pengembalian = db.Column(db.String(225))

    def __init__(self, tanggal_peminjaman, tanggal_pengembalian, created_at, updated_at, deleted_at):
        self.tanggal_peminjaman = tanggal_peminjaman,
        self.tanggal_pengembalian = tanggal_pengembalian,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.deleted_at = deleted_at,

    def __repr__(self):
        return "<id {}>".format(self.id)

   

    