from app import db
from app import app

class Animal(db.Model):
    __tablename__ = "db_animal"

    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(250),nullable = True)
    weight = db.Column(db.String(250),nullable = True)
    specie = db.Column(db.String(250),nullable = True)