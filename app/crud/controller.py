
from flask import jsonify
from app import db
from app.crud.models import Animal
from flask import request

def index():
    params = request.json


    animal = Animal(**params)
    db.session.add(animal)
    db.session.commit()

    return jsonify({
        "STATUS":"DATA INSERTED!",
        "DATA":params
    }),200 