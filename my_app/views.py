from my_app import app
from flask import render_template, request, redirect, Flask, jsonify, json
import requests

@app.route("/")
def index():
    try:
        filename = "challenge.json"
        with open(filename) as challenge:
            data = json.load(challenge)     

    except (ValueError, KeyError, TypeError):
        return render_template("index.html")

    

@app.route("/about_us")
def about_us_page():
    return render_template("about_us.html")

@app.route("/create_event")
def create_event_page():
    return render_template("create_event.html")

@app.route('/add_challenge', methods = ['POST']) 
def add_challenge(): 
   duration_out = request.form['duration']
   emails_out = request.form['emails']
   description_out = request.form['description']
   data = {'duration' : duration_out,'emails' : emails_out,'description': description_out}

   with open("challenge.json", "a") as outfile:
        json.dump(data, outfile) 

   return redirect("/")

