from app import db



class Category(db.Model):
    __tablename__  = "db_category"

    id = db.Column(db.Integer(),primary_key = True,nullable = False)
    name = db.Column(db.String(300),nullable = False)


class Car(db.Model):
    __tablename__  = "db_cars"

    id = db.Column(db.Integer(),primary_key = True,nullable = False)
    name = db.Column(db.String(300),nullable = False)
    quantity = db.Column(db.Integer(),nullable = False)
    category = db.Column(db.Integer(),db.ForeignKey("db_category.id"),nullable = False)
    
    
    

