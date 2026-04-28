from ast import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserCreate, UserRead
from services.user_service import create_user, get_users

router = APIRouter(prefix="/users")

@router.post("/", response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserRead])
def read(db: Session = Depends(get_db)):
    return get_users(db)