from sqlalchemy.orm import Session
import models, schemas

def create_task(db: Session, task: schemas.taskPost):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        done=task.done
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_tasks(db: Session):
    return db.query(models.Task).all()

def update_task(db: Session, task_id: int, task: schemas.taskPost):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.done = task.done
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

def complete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.done = True
        db.commit()
        db.refresh(db_task)
        return db_task
    return None