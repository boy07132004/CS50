import os
import csv
from flask import Flask , request , render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    info = Flight.query.all()
    for flight in info:
        print(f"{flight.origin} to {flight.destination} lasting {flight.duration}minutes.")
    if True:
        print('===================')
        print('select * from flights where  ID = 2;')
        print(Flight.query.filter_by(id=2).first())
        print(Flight.query.get(2))
        print('===================\n')
    if True:
        print('===================')
        print(Flight.query.filter_by(id=2).first().duration)
        print('UPDATE flights SET duration=710 where  ID = 2;')
        flight.query.get(2).duration = 710
        print(Flight.query.get(2).duration)
        print('===================\n')
    if True:
        print('===================')
        print('select * from flights ORDER BY duration DESC;')
        A = Flight.query.order_by(Flight.duration.desc()).all()
        for fl in A:
            print(f"Flight{fl.id} - {fl.origin} to {fl.destination} lasting {fl.duration}minutes.")
        print('===================\n')
    if True:
        print('===================')
        print('select * from flights WHERE origin!=Korea;')
        print(Flight.query.filter(Flight.origin!='Korea').all())
        print('===================\n')
    if True:
        print('===================')
        print('select * from flights join passengers on flights.id = passengers.flights_id;')
        B=db.session.query(Flight,Passenger).filter(Flight.id == Passenger.flight_id).order_by(Flight.id).all()
        for b in B:
            print(f"{b.Flight.origin} to {b.Flight.destination} Passengers:{b.Passenger.name}")
        print('===================\n')
    #commit
    #db.session.commit()

if __name__ =="__main__":
    with app.app_context(): 
        main()