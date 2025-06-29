from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
from services import taskService

router = APIRouter()

@router.post("/", response_model=schemas.taskGet)
def create(task: schemas.taskPost, db: Session = Depends(get_db)):
    return taskService.create_task(db, task)

@router.get("/", response_model=List[schemas.taskGet])
def get_all(db: Session = Depends(get_db)):
    return taskService.get_all_tasks(db)

@router.put("/{task_id}", response_model=schemas.taskGet)
def update_task(task_id: int, task: schemas.taskPost ,db: Session = Depends(get_db)):
    updated = taskService.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="No se encontro la task.")
    return updated

@router.delete("/{task_id}")
def delete_task(task_id : int, db: Session = Depends(get_db)):
    taskService.delete_task(db, task_id)
    return {"detalle" : "Task eliminada."}

@router.patch("/{task_id}")
def complete_task(task_id : int, db: Session = Depends(get_db)):
    completed = taskService.complete_task(db, task_id)
    if not completed:
        raise HTTPException(status_code=404, detail="No se encontro la task.")
    return completed