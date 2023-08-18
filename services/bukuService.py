from app import db
from models.Buku import Buku
from sqlalchemy.sql import text

class BukuService(db.Model):
    __tablename__ = "buku"

    def get_list(filter, page, limit, sortBy):
        search = "%{}%".format(filter)
        data = Buku.query.filter(
            Buku.deleted_at == None,
            Buku.judul_buku.ilike(search)
        )
       
        if sortBy is not None:
            sortBy = sortBy.split(",")
            data = data.order_by(text("{} {}".format(sortBy[0], sortBy[1])))
        paginated_data = data.paginate(page=page, per_page=limit)

        return paginated_data
    
    def get_by_id(id):
        data = Buku.query.filter_by(id = id).first()

        return data
    
    def get_by_buku(buku):
        data = Buku.query.filter_by(buku = buku).first()
        return data
    
    def get_by_judul_buku(judul_buku):
        data = Buku.query.filter_by(judul_buku = judul_buku).first()
        return data
    