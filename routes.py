from app import app,db #import db object and app instance
from flask import render_template,redirect,url_for,flash,get_flashed_messages,redirect,request
import models
import forms
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    tasks=models.Task.query.all()
    return render_template('index.html',tasks=tasks)#can add dynamic text like current_title='Custom xyz title' as an #argument


@app.route('/add',methods=['GET','POST'])
def add():
    form=forms.AddTaskForm()
    #if form submitted ==true
    if form.validate_on_submit():
        task = models.Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        flash('Task added')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
     


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    form = forms.AddTaskForm()
    task = models.Task.query.get(task_id)
    print(task)
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task updated')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    flash(f'Task with id {task_id} does not exit')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    form = forms.DeleteTaskForm()
    task = models.Task.query.get(task_id)
    if task:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(task)
                db.session.commit()
                flash('Task deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    flash(f'Task with id {task_id} does not exit')
    return redirect(url_for('index'))
