from login_app import app
from flask import render_template,redirect,request,session,flash
from login_app.models.user import User