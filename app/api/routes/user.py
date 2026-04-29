from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.user import User
from db.database import get_db
from schemas.user import UserCreate, UserRead
from services.auth_service import get_current_user
from services.user_service import create_user, get_users, delete_user

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserRead)
def create(
        user: UserCreate,
        db: Session = Depends(get_db)):

    return create_user(db, user)


@router.get("/", response_model=list[UserRead])
def read(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):

    return get_users(db)


@router.delete("/{user_id}")
def delete(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):

    user = delete_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User successfully deleted"}


@router.get("/me", response_model=UserRead)
def me(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="You are not authenticated")

    return current_user