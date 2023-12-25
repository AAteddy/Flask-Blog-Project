from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
