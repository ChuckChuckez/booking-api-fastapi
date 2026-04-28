from models.user import User

def create_user(db, user_data):
    user = User(
        email=user_data.email,
        password=user_data.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db):
    return db.query(User).all()