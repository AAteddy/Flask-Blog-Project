from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "d346f2dd7246a059cc2b0d221c1f1200"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
