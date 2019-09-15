import os
import csv
from flask import Flask , request , render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flight.csv")
    reader = csv.reader(f)
    for ori , dest , dur in reader:
        flight = Flight(origin = ori,destination = dest,duration =dur)
        db.session.add(flight)
        print(f"Add flight from {ori} to {dest} lasting {dur}minutes.")
    db.session.commit()
if __name__ =="__main__":
    with app.app_context(): 
        main()