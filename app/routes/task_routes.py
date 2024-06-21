from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app.models.task import Task
from app import db

task_bp = Blueprint('tasks', __name__)


@task_bp.route('/')
def index():
    tasks = Task.query.all()
    events = [{
        'title': task.name,
        'start': task.date.strftime('%Y-%m-%d'),
        'description': task.description
    } for task in tasks]
    return render_template('task_calendar.html', tasks=events)


@task_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['name']
        task_description = request.form['description']
        task_date = request.form['date']
        new_task = Task(name=task_name,
                        description=task_description,
                        date=datetime.strptime(task_date, '%Y-%m-%d'))
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.index'))
    return render_template('add_task.html')


@task_bp.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.name = request.form['name']
        task.description = request.form['description']
        task.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('tasks.index'))
    return render_template('edit_task.html', task=task)


@task_bp.route('/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.index'))
