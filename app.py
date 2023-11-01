from flask import Flask, render_template, request, redirect

from __ini__ import create_app
from task.controllers import TaskController

app = create_app()
task_controller = TaskController()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_controller.create_task()
        return redirect('/')
    if request.method == "GET":
        tasks = task_controller.read_task()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_controller.delete_task(id)
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def  update(id):
    task = task_controller.retrieve_task(id)

    if request.method == 'POST':
        task_controller.update_task(task)
        return redirect('/')
    if request.method == "GET":
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)

# https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
# https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/