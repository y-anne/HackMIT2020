from my_app import app
from flask import render_template, request, redirect
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


