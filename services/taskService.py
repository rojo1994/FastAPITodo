from sqlalchemy.orm import Session
import models, schemas

def create_task(db: Session, task: schemas.taskPost, user_id: int):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        done=task.done,
        owner_id=user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id==user_id).all()

def update_task(db: Session, task_id: int, task: schemas.taskPost, user_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id).first()
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.done = task.done
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

def complete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id).first()
    if db_task:
        db_task.done = True
        db.commit()
        db.refresh(db_task)
        return db_task
    return None