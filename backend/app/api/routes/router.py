from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.core.db.database import get_db

api_router = APIRouter()

@api_router.get("/")
def testing_db(db:Session = Depends(get_db)):
    return {
        "msg": db
    }