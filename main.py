from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/wad"

mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users=mongo.db.users.find({})
    return render_template("mainPage.html",users=online_users)

@app.route("/signup")
def signup_page():
    online_users=mongo.db.users.find({})
    return render_template("signup.html")

@app.route("/authentication")
def auth_page():
    online_users=mongo.db.users.find({})
    return render_template("authentication.html")

@app.route('/post', methods = ['POST'])
def h_page():
    lname = request.form.get("lname")
    fname = request.form.get("fname")
    return render_template("signup.html", lname=lname, fname=fname)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)