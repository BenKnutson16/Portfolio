from flask import render_template, url_for, request, redirect
from models import db, Project, app
from datetime import datetime


def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/<project_id>')
def detail(project_id):
    projects = Project.query.all()
    project = Project.query.get_or_404(project_id)
    return render_template('detail.html', project=project, projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    if request.form:
        project = Project(title=request.form['title'],
                          date=format_date(request.form['date']),
                          description=request.form['description'],
                          skills=request.form['skills'],
                          link=request.form['github'],
                          )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


# Disabled edit and delete functionality for live website
'''
@app.route('/projects/<project_id>/edit', methods=['GET', 'POST'])
def edit(project_id):
    projects = Project.query.all()
    project = Project.query.get_or_404(project_id)
    if request.form:
        project.title = request.form['title']
        project.date = format_date(request.form['date'])
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project, projects=projects)


@app.route('/projects/<project_id>/delete', methods=['GET', 'POST'])
def delete(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))
'''


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', msg=error, projects=projects), 404


def add_old_projects():
    project_1 = Project(title='Number Guessing Game',
                        date=format_date('2022-04-21'),
                        description='This is my first project for Treehouse Techdegree. It is a game where you try to guess the correct number 1-10 in the fewest tries.',
                        skills='Functions, Loops, Exception handling, Input, String formatting, Variable conversion',
                        link='https://github.com/BenKnutson16/Number-Guessing-Game'
                        )

    project_2 = Project(title='Team Stats Tool',
                        date=format_date('2022-05-18'),
                        description='This is my second project for Treehouse Techdegree. It is a tool for cleaning stats for cleaning up player statistics and organizing teams for a group of Basketball players.',
                        skills='File input, Cleaning data, Lists, Dictionaries',
                        link='https://github.com/BenKnutson16/Team-Stats-Tool'
                        )

    project_3 = Project(title='Phrase Hunters',
                        date=format_date('2022-06-13'),
                        description='This is my third project for the Treehouse Techdegree. The goal of the game is to guess a random phrase one letter at a time before you run out of guesses.',
                        skills='Object oriented programming',
                        link='https://github.com/BenKnutson16/Phrase-Hunters'
                        )

    project_4 = Project(title='Store Inventory',
                        date=format_date('2022-08-01'),
                        description='This is my fourth project for the Treehouse Techdegree. This program takes inventory data from a csv file and allows the user to analyze, edit, and backup the data.',
                        skills='Object relational mapping, File input/output, SQL/SQLAlchemy, Managing database',
                        link='https://github.com/BenKnutson16/Store-Inventory'
                        )

    db.session.add(project_1)
    db.session.add(project_2)
    db.session.add(project_3)
    db.session.add(project_4)
    db.session.commit()
    return


if __name__ == '__main__':
    db.create_all()
    current_projects = Project.query.all()
    if len(current_projects) == 0:
        add_old_projects()
    app.run(debug=True, port=8000, host='127.0.0.1')
