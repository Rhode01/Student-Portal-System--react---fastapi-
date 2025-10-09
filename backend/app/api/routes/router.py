from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.api.routes.auth_routes import auth_router
api_router = APIRouter()
api_router.include_router(auth_router)
