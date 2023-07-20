from datetime import datetime
import traceback
from flask_seeder import Seeder
from app import db
from models.role import Role
import uuid

class RoleSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):
        ts = datetime.utcnow()
        try:
            print("adding Role")
            
            role = Role.query.all()
            if len(role) == 0:
                role_data = [
                    Role(
                        id=str(uuid.uuid4()),
                        role="Super Admin",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Kepala Biro",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Kepala Bagian",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Kepala Sub Bagian",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Staff",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Admin Satker",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Admin Pusbinjabfung",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Admin Satker Pustikkp",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                    Role(
                        id=str(uuid.uuid4()),
                        role="Admin TU",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    )
                ]
                db.session.bulk_save_objects(role_data)
                db.session.commit()
        except Exception as e:
           traceback.print_exc()
