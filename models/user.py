from sqlalchemy import ForeignKey
from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import json
import uuid

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    role_id = db.Column(db.String(36), ForeignKey('role.id'))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    gender = db.Column(db.String(255), nullable=True)
    token = db.Column(db.String(255), default=None)
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)
    last_login_at = db.Column(db.DateTime(), nullable=True)

    role = relationship("Role", backref="users")
    # parent_clientId = db.Column(UUID(as_uuid=True), nullable=True)

   

    def __init__(
        self,
        role_id,
        name,
        email,
        password,
        gender,
        token,
        deleted_at,
        created_at,
        updated_at,
        last_login_at,
    ):
        self.name = name
        self.role_id = role_id
        self.email = email
        self.password = password
        self.gender = gender
        self.token = token
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_login_at = last_login_at

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<id {}>".format(self.id)