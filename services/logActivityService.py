import datetime
from app import db
from models.logActivity import LogActivity
from sqlalchemy.sql import text

ts = datetime.datetime.utcnow()

class LogActivityService(db.Model):
    __tablename__ = "log_activity"

    def add_log(user_id, activity):
        log = LogActivity(
            user_id = user_id,
            activity = activity,
            created_at = ts,
            deleted_at= None
        )
        db.session.add(log)
        db.session.commit()
        return log
