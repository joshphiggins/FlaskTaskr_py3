from views import db
from models import Task
from datetime import date

db.create_all()

db.session.add(Task("Finish this tutorial", date(2016, 7, 12), 10, 1))
db.session.add(Task("Finish Real Python Book 2", date(2016, 7, 12), 10, 1))

db.session.commit()