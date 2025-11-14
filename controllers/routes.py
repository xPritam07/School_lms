from flask import render_template, request, redirect, url_for, session, flash, jsonify
from models.model import *
from app import app
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from zoneinfo import ZoneInfo

timezone = ZoneInfo("Asia/Kolkata")
def current_timestamp():
    return datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

def auth_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if 'user_id' not in session:
            flash("Please log in to continue")
            return redirect(url_for('login_page'))
        return func(*args,**kwargs)
    return inner

def admin_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if "user_id" not in session:
            return redirect(url_for('login_page'))
        user=User.query.get(session['user_id'])
        if not user.is_admin:
            flash('You are not a authorized personel')
            return redirect(url_for('login_page'))
        return func(*args,**kwargs)
    return inner

@app.route('/', methods = ['GET', 'POST'])
def home_page():
        return render_template('/before_login/home_page.html')
