from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Home Page'

@app.route('/projects/new')
def create():
    pass

@app.route('/projects/<id>')
def detail():
    pass

@app.route('/projects/<id>/edit')
def edit():
    pass

@app.route('/projects/<id>/delete')
def delete():
    pass



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')