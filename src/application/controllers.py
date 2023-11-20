from ext.database import db
from .models import Todo

from flask import request

class TodoController:

    def __init__(self) -> None:
        pass

    def create(self, task_content):
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
        except Exception:
            return 'There was a problem deleting that task'

    def read(self):
        tasks = Todo.query.order_by(Todo.date_created).all()
        return tasks

    def delete(self, task_id):
        task_to_delete = Todo.query.get_or_404(task_id)

        try:
            db.session.delete(task_to_delete)
            db.session.commit()
        except Exception:
            return 'There was a problem deleting that task'

    def retrieve_task(self, task_id):
        task = Todo.query.get_or_404(task_id) # query by id
        return task
        # return f'testing {task_id}'

    def update(self, task):
        task.content = request.form['content'] # update content with content form

        try:
            db.session.commit() # write updates on database
        except Exception:
            return 'There was an issue updating your task'
