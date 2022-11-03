from flask import Flask, render_template, request, flash
import pandas as pd
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method =="POST":
        username2 =request.form.get("username")
        password2 = request.form.get("password")

        if username2 == password2 == "admin":
            flash("Login Success","success")
            return render_template("register.html")
    else:
        flash("Invalid Login","danger")
        return render_template("login.html")
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/about")
def contact():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        firstname2 = request.form.get("FirstName")
        lastname2 = request.form.get("LastName")
        email2 = request.form.get("Email")
        contact2 = request.form.get("Contact")
        password2 = request.form.get("Password")

        filename = "static/data.csv"
        header = ("FirstName", "LastName", "Email", "Contact", "Password")
        data = [(firstname2, lastname2, email2, contact2, password2)]

        with open(filename, "w", newline="") as csvfile:
            d = csv.writer(csvfile)
            d.writerow(header)
            for x in data:
                d.writerow(x)
    

        return "Data has been Stored Successfully"

    return render_template("home.html")

if __name__ == "__main__":
    app.secret_key = "12345"
    app.run(debug= True)

    

