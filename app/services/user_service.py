from models.user import User
from core.security import  hash_password

def create_user(db, user_data):
    user = User(
        email = user_data.email,
        password = hash_password(user_data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db):
    return db.query(User).all()

def delete_user(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user