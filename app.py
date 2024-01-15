from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/projects/new", methods=['GET', 'POST'])
def create():
    print(request.form)
    return render_template('projectform.html')


@app.route("/projects/<id>")
def detail():
    return render_template('detail.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/projects/<id>/edit")
def edit():
    pass


@app.route("/projects/<id>/delete")
def delete(project_id):
    pass


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
