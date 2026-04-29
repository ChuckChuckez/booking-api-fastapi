from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from models.user import User
from core.security import verify_password, create_access_token, oauth2_scheme, decode_token
from db.database import get_db


def authenticate_user(db, email, password):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user

def login_user(db, email, password):
    user = authenticate_user(db, email, password)

    if not user:
        return None

    token = create_access_token({"sub": user.email})
    return token

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials [token]",
        )

    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials [email]",
        )

    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User does not exist",
        )

    return user