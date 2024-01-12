from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/projects/new")
def create():
    return render_template('projectform.html')


@app.route("/projects/<id>")
def detail():
    pass


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/projects/<id>/edit")
def edit():
    pass


@app.route("/projects/<id>/delete")
def delete():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
