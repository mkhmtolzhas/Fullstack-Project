from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from auth.database import get_async_session, User
from auth.manager import get_user_manager

from auth.auth import auth_backend

from sqlalchemy import select, insert, text
from sqlalchemy.ext.asyncio import AsyncSession

from get_tour.schemas import TourCreate

from get_tour.models import tour

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()



router = APIRouter(
    prefix="/tours",
    tags=["Tour"]
)


# @router.get("/")
# async def get_user_tour(name: str, session: AsyncSession = Depends(get_async_session)):
#     try:
#         query = select(tour).where(tour.c.user_name == name)
#         # print(query)
#         result = await session.execute(query)
#         data = result.fetchall()
#         # data = [(1, 'mkhmtcore', 'Bab Al Bahr', 200000)]
#         print(data)
#         json_data = [[{'id': item[0], 'name': item[1], 'tour_name': item[2], 'price': item[3]} for item in data] for i in range(len(data))]
#         return json_data[0]

#     except Exception as e:
#         print(e)

@router.get("/active_user_tours")
async def get_active_user_tour(user : User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(tour).where(tour.c.user_name == user.email)
        result = await session.execute(query)
        data = result.fetchall()
        json_data = [[{'id': item[0], 'tour_name': item[1], 'price': item[2], 'name': item[3]} for item in data] for i in range(len(data))]
        return json_data[0]

    except Exception as e:
        print(e)


@router.post("/add_tour_for_user")
async def add_active_user_tour(create : TourCreate, user : User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    try:
        values = create.dict()
        query = text("select count(*) from tour")
        length = await session.execute(query)
        values["user_name"] = user.email
        values["id"] = length.scalar() + 1
        stmt = insert(tour).values(**values)
        await session.execute(stmt)
        await session.commit()
        return {"status" : True}
    except Exception as e:
        print(e)