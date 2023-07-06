from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from data_contract.user import *

from models.userdb import *
from settings import error_responses, ACCESS_TOKEN_EXPIRE_MINUTES

api_router = APIRouter()


@api_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@api_router.get("/users/me/", response_model=UserDetailOut)
def read_users_me(current_user: UserDetailOut = Depends(get_current_active_user)):
    return current_user


@api_router.post("/create/", response_model=UserShortOut, responses=error_responses)
def user_create(in_manager: UserCreateIn):
    out_manager = create_user(in_manager)

    return out_manager
