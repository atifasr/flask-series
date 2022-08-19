
from unicodedata import category
from flask import jsonify,request
from app import db
from app.crud.models import Car,Category

def create():

    params = request.json
    car = Car(name = params['name'],quantity = params['quantity'],category= params['category'])    
    db.session.add(car)
    db.session.commit()

    return jsonify({"STATUS":"OK","message":"row has been inserted","data":params}),200


def create_category():
    params = request.json
    category = Category(name = params['name'])    
    db.session.add(category)
    db.session.commit()

    return jsonify({"STATUS":"OK","message":"row has been inserted","data":params}),200


def get_cars():

    cars = db.session.query(Car.id,Car.name,Car.quantity,Category.name.label("category_name")).\
        outerjoin(Category,Car.category == Category.id).all()

    cars = [{
        'id':row.id,
        'name':row.name,
        'quantity':row.quantity,
        'category_name':row.category_name,

    } for row in cars]
    return jsonify({"STATUS":"OK","message":"row has been inserted","data":cars}),200


def read():
    cars = db.session.query(Car).all()
    cars = [ 
        {
            'name':car.name,
            'id':car.id,
            'quantity':car.quantity,
        } 
            for car in cars ] 

    return jsonify({"STATUS":"OK","data":cars}),200

