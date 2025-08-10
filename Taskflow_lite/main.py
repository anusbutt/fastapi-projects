from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Task, TaskCreate

app = FastAPI()

tasks_db: List[Task] = []
task_id_counter = 1


@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_data = updated_task.dict()
            merged_task = Task(
                id=task_id,
                name=updated_data.get("name", task.name),
                description=updated_data.get("description", task.description),
                completed=updated_data.get("completed", task.completed)
            )
            tasks_db[i] = merged_task
            return merged_task
    raise HTTPException(status_code=404, detail="task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[i]
            return {"message": "task deleted"}
    raise HTTPException(status_code=404, detail="task not found")
