from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/Register")
def Register():
    return render_template("Register.html")

@app.route("/About")
def About():
    return render_template("About.html")

if __name__ == "__main__" :
    app.run(debug=True)
