from flask import Blueprint, request, render_template
from .task import Task
from . import db

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template("int.html")

@main.get("/tasks")
def get_current_tasks():
    tasks = Task.query.all()

    tasklist = []

    for task in tasks:
        tasklist.append({
            "id": task.id,
            "task": task.task,
            "status": task.status
        })
    return tasklist

@main.post("/tasks/add")
def add_tasks():
    data = request.get_json()
    new_task = Task()
    new_task.task = data["task"]
    db.session.add(new_task)
    db.session.commit()
    return {"message": "Tasks added successfully"}, 200
    

@main.delete("/tasks/delete/<int:t_id>")
def delete_task(t_id):
    tasks = Task.query.filter(Task.id ==t_id)
    if tasks == None:
        return{"message": "Task not found"}, 401
    db.session.delete(tasks)
    db.session.commit()
    return {"message": "Task deleted successfully"}, 200

@main.put("/task/edit/<int:task_id>")
def edit_task(task_id):
    task = Task.query.filter(Task.id == task_id).first()
    if task == None:
        return{
            "message": "No tasks found"
        }, 401
    task.status = True
    db.session.commit()
    return {"message": "Task completed Successfully"}, 200