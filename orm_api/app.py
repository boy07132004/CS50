import os

from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    name =  request.form.get("name")
    try:
        fid = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",code="You are arrested")
    info = Flight.query.get(fid)
    if info is None:
        return render_template("error.html",code="No such flight")
    else:
        """ OLD VERSION
        passenger = Passenger(name = name,flight_id =fid)
        db.session.add(passenger)
        db.session.commit()
        """
        info.add_passenger(name)
        return render_template("book.html",name=name,ori=info.origin,dest=info.destination)

@app.route("/flights")
#List All flights
def flights():
    flights = Flight.query.all()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html",code = "Error flight_id")
    #passengers = Passenger.query.filter(Passenger.flight_id == flight_id)
    passengers = flight.passengers
    return render_template("flight.html",passengers=passengers,flight=flight)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    flight = Flight.query.get(flight_id)
    
    # Make sure flight exists.
    if flight is None:
        return jsonify({"error":"Invalid flight_id"}),422
    
    # Get all passengers
    passengers = flight.passengers
    name = []
    for passenger in passengers:
        name.append(passenger.name)
    return jsonify({
        "flight":flight_id,
        "origin":flight.origin,
        "destination":flight.destination,
        "duration":flight.duration,
        "passenger":name
    }
    )
