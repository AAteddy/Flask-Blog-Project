from flask import flash, redirect, render_template, url_for
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in.", "success")
        return redirect(url_for("login"))
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
