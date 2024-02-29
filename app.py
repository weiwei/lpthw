from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

@app.route('/')
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START

    return redirect(url_for("game"))

@app.route('/game', methods=['GET', 'POST'])
def game():
    # The main
    room_name = session.get('room_name')
    if room_name:
