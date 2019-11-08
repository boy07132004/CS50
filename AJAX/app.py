import os

from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=["POST"])
def search():
    username = request.form.get("username")
    res = requests.get(r"https://jsonplaceholder.typicode.com/users",params={"username":username})

    if res.status_code !=200:
        return jsonify({"success":False})
    data = res.json()
    return jsonify({"success":True,"id":data[0]["id"],"username":username})