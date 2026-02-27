from flask import Flask, render_template

from music_chart_flask import database

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def home():
    return render_template("index.html", songs = database.get())


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)