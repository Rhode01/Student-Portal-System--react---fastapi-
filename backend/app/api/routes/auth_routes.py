from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db.database import get_db
from app.schemas.user_schema import UserLoginSchema,UserSchema
from app.crud.user_crud import UserCRUD
from app.utils.protection import get_current_user
from app.schemas.user_schema import UserOutSchema

auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@auth_router.post("/register")
async def register_user(user: UserSchema, db: AsyncSession = Depends(get_db)):
    crud = UserCRUD(db)
    result = await crud.create_new(user)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
@auth_router.post("/login")
async def login_user(credentials: UserLoginSchema, db: AsyncSession = Depends(get_db)):
    crud = UserCRUD(db)
    result = await crud.login_user(credentials)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result
    
@auth_router.get("/me", response_model=UserOutSchema)
async def get_profile(current_user = Depends(get_current_user)):
    return current_user
