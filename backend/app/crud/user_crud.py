from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from app.core.db.crud.base_crud import BaseCRUD
from app.schemas.user_schema import UserSchema, UserLoginSchema
from app.models.user import User
from app.core.security.security import hash_password, verify_password, create_access_token


class UserCRUD(BaseCRUD[User]):
    def __init__(self, db: AsyncSession):
        super().__init__(User, db)

    async def create_new(self, details: UserSchema):
        result = await self.db.execute(
            select(self.model).filter(self.model.username == details.username)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            return {"error": "User already exists", "status": HTTP_400_BAD_REQUEST}

        hashed_pwd = hash_password(details.password)
        new_user = self.model(
            username=details.username,
            password=hashed_pwd,
            role=details.role,
        )

        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)

        return {"data": new_user, "status": HTTP_201_CREATED}

    async def login_user(self, details: UserLoginSchema):
        result = await self.db.execute(
            select(self.model).filter(self.model.username == details.username)
        )
        user = result.scalar_one_or_none()

        if not user or not verify_password(details.password, user.password):
            return {"error": "Invalid username or password", "status": HTTP_401_UNAUTHORIZED}

        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
