from typing import Type, TypeVar, Generic, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.db.database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseCRUD(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db

    async def get_all(self) -> List[ModelType]:
        result = await self.db.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, id: int) -> Optional[ModelType]:
        result = await self.db.execute(select(self.model).filter(self.model.id == id))
        return result.scalar_one_or_none()

    async def create(self, obj_in) -> ModelType:
        obj = self.model(**obj_in.dict())
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def update(self, id: int, obj_in) -> Optional[ModelType]:
        db_obj = await self.get_by_id(id)
        if not db_obj:
            return None

        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)

        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def delete(self, id: int) -> bool:
        db_obj = await self.get_by_id(id)
        if not db_obj:
            return False

        await self.db.delete(db_obj)
        await self.db.commit()
        return True
