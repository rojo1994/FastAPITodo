from sqlalchemy.orm import Session
import schemas, auth, models

def create_user(db: Session, user: schemas.UserPost):
    hashed_pw = auth.get_hashed_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user