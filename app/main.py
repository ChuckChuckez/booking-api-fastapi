from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from api.routes import user, auth
from db.database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"message": "DB connected"}