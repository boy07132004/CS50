import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db     = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights ORDER BY id").fetchall()
    return render_template("index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    name =  request.form.get("name")
    try:
        fid = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",code="You are arrested")
    info = db.execute(f"SELECT * FROM flights WHERE id={fid}").fetchone()
    if info is None:
        return render_template("error.html",code="No such flight")
    else:
        db.execute("INSERT INTO passengers (name,flight_id) VALUES (:name,:flight_id)",{"name":name,"flight_id":fid})
        db.commit()
        return render_template("book.html",name=name,ori=info.origin,dest=info.destination)