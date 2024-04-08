from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import Session
from flask import abort

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'
    
    @classmethod
    def get_or_404(cls, id):
        plant = db.session.query(cls).get(id)
        if plant is None:
            abort(404)
        return plant