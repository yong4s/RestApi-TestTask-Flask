from app import app
from flask import request, jsonify
from .schemas import DriverSchema, VehicleSchema
from .models import db, Driver, Vehicle


driver_schema, vehicle_schema = DriverSchema(), VehicleSchema()
drivers_schema, vehicles_schema = DriverSchema(many=True), VehicleSchema(many=True)

@app.route('/drivers/driver', methods=['GET', 'POST'])
def post_get_driver():
    if request.method == 'POST':
        first_name = request.json['first_name']
        last_name = request.json['last_name']

        my_driver = Driver(first_name, last_name)
        db.session.add(my_driver)
        db.session.commit()

        return driver_schema.jsonify(my_driver)

    if request.method == 'GET':
        all_driver = Driver.query.all()
        result = drivers_schema.dump(all_driver)

        return jsonify(result)


@app.route('/vehicles/vehicle', methods=['GET', 'POST'])
def post_get_vehicle():
    if request.method == 'POST':
        make = request.json['make']
        model = request.json['model']
        plate_number = request.json['plate_number']

        my_vehicle = Vehicle(make, model, plate_number)
        db.session.add(my_vehicle)
        db.session.commit()

        return vehicle_schema.jsonify(my_vehicle)

    if request.method == 'GET':
        all_vehicles = Vehicle.query.all()
        result = vehicles_schema.dump(all_vehicles)

        return vehicle_schema.jsonify(result)




@app.route('/drivers/driver/<id>/', methods=['GET', 'DELETE', 'PUT'])
def get_del_put_drivers(id):
    if request.method == 'GET':
        driver = Driver.query.get(id)


    if request.method == 'DELETE':
        driver = Driver.query.get(id)
        db.session.delete(driver)

    if request.method == 'PUT':
        driver = Driver.query.get(id)

        first_name = request.json['first_name']
        last_name = request.json['last_name']

        driver.first_name = first_name
        driver.last_name = last_name

    db.session.commit()
    return driver_schema.jsonify(driver)


@app.route('/vehicles/vehicle/<id>/', methods=['GET', 'DELETE', 'PUT'])
def get_del_put_vehicles(id):
    if request.method == 'GET':
        vehicle = Vehicle.query.get(id)

    if request.method == 'DELETE':
        vehicle = Vehicle.query.get(id)
        db.session.delete(vehicle)

    if request.method == 'PUT':
        vehicle = Vehicle.query.get(id)

        make = request.json['make']
        model = request.json['model']
        plate_number = request.json['plate_number']

        vehicle.make = make
        vehicle.model = model
        vehicle.plate_number = plate_number

    db.session.commit()

    return vehicle_schema.jsonify(vehicle)


@app.route('/drivers/driver/', methods=['GET'])
def get_drivers():
    created_at__gte = request.args.get('created_at__gte')
    created_at__lte = request.args.get('created_at__lte')
    if created_at__gte == '10-11-2021':
        date = db.session.query(Driver).filter(Driver.created_at > '2021-11-10')

    elif created_at__lte == '16-11-2021':
        date = db.session.query(Driver).filter(Driver.created_at < '2021-11-16')

    return drivers_schema.jsonify(date)


@app.route('/vehicles/vehicle/', methods=['GET'])
def get_vehicles():
    with_driver = request.args.get("with_driver")
    if with_driver == 'yes':
        with_drivers = db.session.query(Vehicle).filter(Vehicle.driver_id > '0')

    elif with_driver == 'no':
        with_drivers = db.session.query(Vehicle).filter(Vehicle.driver_id == None)

    return vehicles_schema.jsonify(with_drivers)

@app.route('/vehicles/<id>/set_driver', defaults={'driver_id': None}, methods=['POST'])
@app.route('/vehicles/<id>/set_driver/<driver_id>/', methods=['POST'])
def set_driver(id, driver_id):
    vehicle = Vehicle.query.get(id)
    vehicle.driver_id = driver_id
    db.session.add(vehicle)
    db.session.commit()
    vehicle
    return jsonify()

