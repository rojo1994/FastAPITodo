from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import schemas, auth
from database import get_db
from services import userService

router = APIRouter()

@router.post("/register", response_model=schemas.UserGet)
def register(user: schemas.UserPost, db: Session = Depends(get_db)):
    return userService.create_user(db, user)

@router.post("/authenticate", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales invalidas.")
    token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}