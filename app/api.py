from flask import Blueprint, request, jsonify, render_template
from task import tasks, get_current_task

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template("int.html")

@main.get("/tasks")
def get_current_tasks():
    return tasks, 201

@main.post("/tasks/add")
def add_tasks():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"],
        "status": False
    }
    tasks.append(new_task)
    return new_task, 201

@main.get("/tasks/delete/<int:t_id>")
def delete_task(t_id):
    task = get_current_task(t_id)
    if task is None:
        return {"message": "No task found"}, 400
    tasks.remove(task)
    return {"message": "Task has been deleted"}, 201

@main.post("/task/edit/<int:task_id>")
def edit_task(task_id):
    task = get_current_task(task_id)
    if task == None:
        return {"message": "No tasks found"}, 400
    data = request.get_json()
    task["status"] = data.get("status", task["status"])
    return task