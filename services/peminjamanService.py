from app import db
from models.peminjaman import Peminjaman
from sqlalchemy.sql import text

class peminjamanService(db.Model):
    __tablename__ = "peminjaman"

    def get_list(filter, page, limit, sortBy):
        search = "%{}%".format(filter)
        data = Peminjaman.query.filter(
            Peminjaman.deleted_at == None,
            Peminjaman.jumlah_bayar.ilike(search)
        )
       
        if sortBy is not None:
            sortBy = sortBy.split(",")
            data = data.order_by(text("{} {}".format(sortBy[0], sortBy[1])))
        paginated_data = data.paginate(page=page, per_page=limit)

        return paginated_data
    
    def get_by_id(id):
        data = Peminjaman.query.filter_by(id = id).first()

        return data
