from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/wad"

mongo = PyMongo(app)
# ------------------Home Page------------------
@app.route("/")
def home_page():
    online_users=mongo.db.users.find({})
    return render_template("mainPage.html",users=online_users)

# ------------------Sign Up & Log In------------------
@app.route("/signup", methods=['GET', 'POST'])
def signup_page():
    online_users=mongo.db.users.find({})
    if request.method == 'GET':
       return render_template("signup.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        if mongo.db.users.count_documents({'username':username}) !=0:
           flash('Username exists! Try again')
           return redirect('signup')

        else:
            mongo.db.users.insert_one({
             'username': username,
             'password': password
            })
            flash('Sign Up!')
            return redirect('/')

@app.route("/authentication")
def auth_page():
    online_users=mongo.db.users.find({})
    return render_template("authentication.html")

'''
@app.route('/post', methods = ['POST'])
def h_page():
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("signup.html", username=username, password=password)
'''

# ------------------set the 404 status explicity------------------
@app.errorhandler(404)  
def page_not_found():
    return render_template("404.html") 

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)