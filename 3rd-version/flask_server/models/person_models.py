
from flask_server.databases.util_db import db_util

class Person(db_util.Model):
    id = db_util.Column(db_util.Integer, primary_key=True)
    name = db_util.Column(db_util.String(255), nullable=False)
    surname = db_util.Column(db_util.String(255), nullable=False)
    phone = db_util.Column(db_util.String(8), nullable=False)
    address = db_util.Column(db_util.String(255), nullable=False)
    age = db_util.Column(db_util.Integer, nullable=False)

    def __repr__(self):
        return f"<Person {self.name} {self.surname}>"

    @classmethod
    def clear_table(cls):
        # Clear all data from the chosen table.
        db_util.session.query(cls).delete()
        db_util.session.commit()
