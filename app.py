#Allways in School Squad
#Softdev PD 8

import hashlib, csv, os
from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def index():
    if 'userA' in session:
        return render_template("home.html", user=session["userA"])
    return redirect(url_for('login'))

@app.route("/login")
def login():
    createdict()
    return render_template("form.html")

@app.route("/logout")
def logout():
    session.pop('userA')
    return redirect(url_for('login'))

csv = "data/users.csv"
storage = dict()

def createdict():
    sdata = open(csv).read()
    sdata = sdata.split(';')
    sdata[:] = [x.split(',') for x in sdata]
    for i in sdata:
        storage[i[0]] = i[1]

def hasher(passw):
    return hashlib.sha224(passw.encode('utf-8')).hexdigest()
    
@app.route("/auth", methods=['POST'])
def authenticate():
    userA = request.form["username"]
    passA = request.form["password"]
    if userA in storage:
        if hasher(passA) == storage[userA]:
            session['userA'] = userA 
            return render_template("home.html", user=session['userA'])
        else:
            return render_template("success.html", result="*Password is incorrect*")
    else:
        return render_template("success.html", result="The username does not exist. Please create an account.")

@app.route("/new", methods=['POST'])
def new():
    return render_template("create.html")


@app.route("/create", methods=['POST'])
def create():
    userA = request.form["username"]
    passA = request.form["password"]
    fd = open(csv, 'a')
    if userA in storage:
        return render_template("success.html", result="An account with that username already exists. Enter the correct password at sign in or make a new account.")
    fd.write(";"+userA+","+hasher(passA))
    fd.close()
    return render_template("success.html", result="Account was successfully created!")

if __name__ == "__main__":
    app.debug = True
    app.run()    
