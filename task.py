tasks = []

def get_current_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None