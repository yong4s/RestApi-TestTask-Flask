from app import app
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
    vehicles = db.relationship('Vehicle', backref='driver')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.created_at = created_at
        # self.updated_at = updated_at


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer(), primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    make = db.Column(db.String())
    model = db.Column(db.String())
    plate_number = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())\

    def __init__(self, make, model, plate_number, created_at, updated_at):
        self.make = make
        self.model = model
        self.plate_number = plate_number
        self.created_at = created_at
        self.updated_at = updated_at



