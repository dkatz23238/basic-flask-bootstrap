from app import db
import datetime

print(datetime.datetime.now())
# ApplicationUser(user_id=0001, username="dk", password="ps")

class ApplicationUser(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class RoboticProcessAutomation(db.Model):
    __tablename__ = "bots"
    rpa_id = db.Column(db.String(36), primary_key=True, unique=True)
    rpa_name = db.Column(db.String(40))
    creation_date = db.Column(db.DateTime())
    git_repository = db.Column(db.String(40))
    cron_fmat_schedule = db.Column(db.String(9))

    def __repr__(self):
        return '<RPA %r>' % self.rpa_name


class RobotRunEvent(db.Model):
    __tablename__ = "botevents"
    event_id = db.Column(db.String(36), unique=True, primary_key=True)
    rpa_id = db.Column(db.String(36), db.ForeignKey('bots.rpa_id'))
    event_datetime = db.Column(db.DateTime())
    tag = db.Column(db.String())
    message = db.Column(db.String())

    def __repr__(self):
        return '<Event %r>' % self.event_id
