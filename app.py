from flask import Flask, request
from task import tasks, get_current_task

app = Flask(__name__)

@app.get("/tasks")
def get_current_tasks():
    return tasks, 201

@app.post("/tasks/add")
def add_tasks():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"],
        "status": False
    }
    tasks.append(new_task)
    return new_task, 201

@app.get("/tasks/<int:t_id>/delete")
def delete_task(t_id):
    task = get_current_task(t_id)
    if task is None:
        return {"message": "No task found"}, 400
    tasks.remove(task)
    return {"message": "Task has been deleted"}, 201

@app.post("/task/<int: task_id>/edit")
def edit_task(task_id):
    task = get_current_task(task_id)
    if task == None:
        return {"message": "No tasks found"}, 400
    data = request.get_json()
    task["status"] = data.get("status", task["status"])
    return task

if __name__ == "__main__":
    app.run(debug= True)