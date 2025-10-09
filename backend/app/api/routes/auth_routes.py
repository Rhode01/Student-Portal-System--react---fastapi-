from fastapi import APIRouter, Depends
from fastapi import  Depends
from starlette.status import HTTP_401_UNAUTHORIZED
from sqlalchemy.orm import Session
from app.core.security.security import verify_password, create_access_token
from app.core.db.database import get_db
from app.schemas.user_schema import UserLoginSchema
from app.models.user import User

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/login")

def login_user(details: UserLoginSchema, db: Session = Depends(get_db)):
        user = db.query(User).filter(
            User.username == details.username
        ).first()

        if not user or not verify_password(details.password, user.password):
            return {"error": "Invalid username or password", "status": HTTP_401_UNAUTHORIZED}

        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    
# @router.get("/me")
# async def get_profile(current_user = Depends(get_current_user)):
    # return current_user
