from flask import render_template, url_for, request, redirect
from models import db, Project, app

@app.route("/")
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


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
def detail(id):
    project = Project.query.get(id)
    project.skills = project.skills.split(',')
    return render_template('detail.html', project=project)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/projects/<id>/edit", methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.date = request.form['date']
        project.descrip = request.form['desc']
        project.skills = request.form['skills']
        project.ghlink = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project)


@app.route("/projects/<id>/delete")
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")
