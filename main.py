from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import UserBase, TaskCreate, TaskResponse
from crud import UserCRUD, TaskCRUD

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the To-Do App"}

@app.post("/users/")
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return UserCRUD(db).create_user(user)

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return UserCRUD(db).get_all_users()

@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskCRUD(db).create_task(task)

@app.get("/tasks/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return TaskCRUD(db).get_all_tasks()

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return TaskCRUD(db).get_task(task_id)
