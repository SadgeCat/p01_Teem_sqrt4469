# Yuhang Pan (PM), Matthew Ciu, Michelle Chen, Thomas Mackey
# Hero Wars by Teem_sqrt4469
# SoftDev
# P01: ArRESTed Development
# 2025-12-03

from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for

import sqlite3

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()      

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for("home"))

    return redirect(url_for("login"))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip().lower()
        password = request.form.get('password').strip()

        # reload page if no username or password was entered
        if not username or not password:
            return render_template("register.html", error="No username or password inputted")

        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        # check if username already exists and reload page if it does
        exists = c.execute("SELECT 1 FROM users WHERE name = ?", (username,)).fetchone()
        if exists:
            db.close()
            return render_template("register.html", error="Username already exists")

        c.execute("INSERT INTO users (name, bio, password) VALUES (?, ?, ?)", (username, "temp bio", password))
        db.commit()
        db.close()

        session['username'] = username
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # store username and password as a variable
        username = request.form.get('username').strip().lower()
        password = request.form.get('password').strip()

        # render login page if username or password box is empty
        if not username or not password:
            return render_template('login.html', error="No username or password inputted")

        #search user table for password from a certain username
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        account = c.execute("SELECT password FROM users WHERE name = ?", (username,)).fetchone()
        db.close()

        #if there is no account then reload page
        if account is None:
            return render_template("login.html", error="Username or password is incorrect")

        # check if password is correct, if not then reload page
        if account[0] != password:
            return render_template("login.html", error="Username or password is incorrect")

        # if password is correct redirect home
        session["username"] = username
        return redirect(url_for("home"))

    return render_template('login.html')
