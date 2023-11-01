from flask import request

from __ini__ import db
from .models import Todo

class TaskController:
    def __init__(self) -> None:
        pass

    def create_task(self):
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
        except:
            return "Something went wrong with your task!"

    def read_task(self):
        tasks = Todo.query.order_by(Todo.date_created).all()
        return tasks

    def retrieve_task(self, id):
        task = Todo.query.get_or_404(id) # query by id
        return task

    def update_task(self, task):
        task.content = request.form['content'] # update content with content form

        try:
            db.session.commit() # write updates on database
        except:
            return 'There was an issue updating your task'

    def delete_task(self, id):
        task_to_delete = Todo.query.get_or_404(id)

        try: 
            db.session.delete(task_to_delete)
            db.session.commit()
        except:
            return 'There was a problem deleting that task'
    