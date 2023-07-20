from app import db
from models.role import Role
from sqlalchemy.sql import text

class RoleService(db.Model):
    __tablename__ = "role"

    def get_list(filter, page, limit, sortBy):
        search = "%{}%".format(filter)
        data = Role.query.filter(
            Role.deleted_at == None,
            Role.role.ilike(search)
        )
       
        if sortBy is not None:
            sortBy = sortBy.split(",")
            data = data.order_by(text("{} {}".format(sortBy[0], sortBy[1])))
        paginated_data = data.paginate(page=page, per_page=limit)

        return paginated_data
    
    def get_by_id(id):
        data = Role.query.filter_by(id = id).first()

        return data
    
    def get_by_role(role):
        data = Role.query.filter_by(role = role).first()
        return data