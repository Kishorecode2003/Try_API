from sqlalchemy.orm import Session
from models import User, Task
from fastapi import HTTPException, status

class UserCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user):
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_all_users(self):
        return self.db.query(User).all()

class TaskCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task):
        if task.status not in ["pending", "completed"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Status must be 'pending' or 'completed'"
            )
        db_task = Task(**task.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_task(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return task

    def get_all_tasks(self):
        return self.db.query(Task).all()
