from app import app, db


class Texts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chars = db.Column(db.String)
    frequency = db.Column(db.Float)
    type =db.Column(db.String, index=True)
