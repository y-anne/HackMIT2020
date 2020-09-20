from my_app import app
from flask import render_template, request, redirect, Flask, jsonify, json
import requests

@app.route("/")
def index():
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
   data = {'duration' : duration_out,
            'emails' : emails_out,
            'description': description_out
            }
    return jsonify(data)

   #print(duration_out)
   #print(emails_out)
   #print(description_out)
   #return redirect("/")

