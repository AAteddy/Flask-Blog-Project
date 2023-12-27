from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "d346f2dd7246a059cc2b0d221c1f1200"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "This is the content of blog post 1",
        "date_posted": "April 24, 2021",
    },
    {
        "author": "Calvert Lowe",
        "title": "Blog Post 2",
        "content": "This is the content of blog post 2",
        "date_posted": "May 15, 2021",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "password":
            flash(f"You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed. Please check your credentials.", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
