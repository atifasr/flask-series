
from app.crud.controller import create,read,create_category,get_cars
from app import app



app.add_url_rule("/create_cars/",'create',create,methods =['POST'])
app.add_url_rule("/read/",'read',read,methods =['GET'])
app.add_url_rule("/create_category/",'create_category',create_category,methods =['POST'])
app.add_url_rule("/get_cars/",'get_cars',get_cars,methods =['GET'])


