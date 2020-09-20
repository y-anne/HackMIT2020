from my_app import app
from flask import render_template, request, redirect, Flask, jsonify, json
import requests

list_of_challenges = [{"duration" : "1"}]
file = open("challenge.txt", "a+")
file.close()
@app.route("/")
def index():
    global list_of_challenges
    for readLine in open("challenge.txt"):
        tasks = readLine.split(",")
        data = {
            "duration" : tasks[0],
            "emails" : tasks[1],
            "descriptions" : tasks[2].strip()
        }
        list_of_challenges.append(data)
            
    return render_template("index.html", list_of_challenges = list_of_challenges)

    

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

   with open("challenge.txt", "a") as outfile:
        s = duration_out + "," + emails_out + "," + description_out + "\n"
        outfile.write(s)
    
   return redirect("/")

