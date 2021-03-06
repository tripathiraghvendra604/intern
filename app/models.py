from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    contact = db.Column(db.Integer , index=True, unique=True)
    city = db.Column(db.String(120), index=True)
    company = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<User %r>' % (self.name)