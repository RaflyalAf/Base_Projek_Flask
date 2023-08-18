from datetime import datetime
import traceback
from flask_seeder import Seeder
from app import db
from models.Buku import Buku
import uuid

class BukuSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):
        ts = datetime.utcnow()
        try:
            print("adding Buku9")
            
            buku = Buku.query.all()
            if len(buku) == 0:
                buku_data = [
                    Buku(
                        judul_buku=" Cantik Itu Luka",
                        kategori_buku = "Novel",
                        penerbit = "Gramedia Pusaka Utama",
                        pengarang = "Eka kurniawan",
                        created_at=ts,
                        deleted_at=None,
                        updated_at=None
                    ),
                   
                ]
                db.session.bulk_save_objects(buku_data)
                db.session.commit()
        except Exception as e:
           traceback.print_exc()
