from fastapi import FastAPI, HTTPException
from schemas import Todo
from typing import List

app = FastAPI()

Todos: List[Todo] = [] 

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    Todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
def get_all_tasks():
    return Todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_task_by_id(todo_id: int):
    for todo in Todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(Todos):
        if todo.id == todo_id:
            Todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int):
    for index, todo in enumerate(Todos):
        if todo.id == todo_id:
            del Todos[index]
            return {"detail": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
