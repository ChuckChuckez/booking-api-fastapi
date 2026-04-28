from ast import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserCreate, UserRead
from services.user_service import create_user, get_users, delete_user

router = APIRouter(prefix="/users")

@router.post("/", response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserRead])
def read(db: Session = Depends(get_db)):
    return get_users(db)

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User successfully deleted"}