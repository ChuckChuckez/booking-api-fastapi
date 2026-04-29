from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.database import get_db
from services.auth_service import login_user
from schemas.user import UserCreate
from services.user_service import create_user

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(
        form_data:OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):
    token = login_user(db, form_data.username, form_data.password)

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {"access_token": token}