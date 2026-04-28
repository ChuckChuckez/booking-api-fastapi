from models.user import User
from core.security import verify_password, create_access_token

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