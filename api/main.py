from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from auth.database import User
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
# current_active_verified_user = fastapi_users.current_user(active=True, verified=True)



app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"

@app.get("/unprotected-route")
def protected_route():
    return f"Hello, Newbie!"



# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_active_verified_user)):
#     return f"Hello, {user.email}"
