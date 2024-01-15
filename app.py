from flask import render_template, url_for, request, redirect
from models import db, Project, app

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/projects/new", methods=['GET', 'POST'])
def create():
    if request.form:
        print(request.form)
        new_proj = Project(title=request.form['title'], date=request.form['date'], descrip=request.form['desc'],
                           skills=request.form['skills'], ghlink=request.form['github'])
        db.session.add(new_proj)
        db.session.commit()
        return redirect(url_for('index'))
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
    app.app_context().push()
    db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")
