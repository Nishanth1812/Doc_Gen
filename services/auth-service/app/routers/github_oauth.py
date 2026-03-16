from fastapi import APIRouter,HTTPException

from app.utils.crypto import create_session_jwt
from app.services.github_client import (
    get_authorization_url,
    exchange_code_for_token,
    get_user_profile,
)
from app.services.session_service import create_user, update_user

router = APIRouter()


@router.get("/login")
def login(state: str):
    url = get_authorization_url(state=state)
    return {"redirect_url": url}


@router.get("/callback")
async def callback(code: str, state: str = None):
    # CSRF is not used when authenticating via Authorization header JWTs.
    token = await exchange_code_for_token(code)
    user = await get_user_profile(token)
    user_id = await update_user(user, token)
    session_jwt = create_session_jwt(user_id=user_id)

    return {"access_token": session_jwt, "token_type": "bearer"}


@router.post("/logout")
def logout():
    # With JWTs in Authorization header, logout is a client-side operation.
    return {"message": "Logged Out"}