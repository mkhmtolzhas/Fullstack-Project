from fastapi_users import schemas
from typing import Optional
from datetime import datetime


from pydantic import ConfigDict
from pydantic.version import VERSION as PYDANTIC_VERSION
PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    ordered_tour: str = None
    registered_at: datetime = datetime.utcnow()
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    ordered_tour: Optional[str] = None
    registered_at: Optional[datetime] = datetime.utcnow()
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass