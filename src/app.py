from flask import Flask, render_template, request, redirect
from .ext import configuration
from .ext import database
from .application.controllers import TodoController

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    controller = TodoController()

    if request.method == "POST":
        task_content = request.form['content']
        controller.create(task_content)
        return redirect('/')

    if request.method == "GET":
        tasks = controller.read()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    controller = TodoController()
    controller.delete(task_id)
    return redirect('/')

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    controller = TodoController()
    task = controller.retrieve_task(task_id)
    if request.method == 'POST':
        controller.update(task)
        return redirect('/')
    else:
        return render_template('update.html', task=task)
