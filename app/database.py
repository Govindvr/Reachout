from app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 50), nullable = False, unique = True)
    password = db.Column(db.String(length = 50), nullable = False)
    name = db.Column(db.String(length = 50), nullable = False)
    email = db.Column(db.String(length = 50), nullable = False, unique = True)
    phno = db.Column(db.String(length = 20), nullable = False, unique = True)
    education_status = db.Column(db.String(length = 100), nullable = False)
    field = db.Column(db.String(length = 500), nullable = False)
    projects = db.Column(db.String(length = 1000))

    def __repr__(self):
        return f'User {self.name}'