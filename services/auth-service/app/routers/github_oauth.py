from fastapi import APIRouter,Request,Response,HTTPException
from fastapi.responses import RedirectResponse 

from app.utils.crypto import create_csrf_token,verify_csrf_token,create_session_jwt 
from app.services.github_client import (get_authorization_url,exchange_code_for_token,get_user_profile)
from app.services.session_service import create_user,update_user

router=APIRouter()

@router.get("/csrf")
def get_csrf():
    token=create_csrf_token()
    return {"csrf_token":token}

@router.get("/login")
def login(state:str):
    
    url=get_authorization_url(state=state)
    
    return {
        "redirect_url":url
    } 
    

@router.get("/callback")
async def callback(code:str,state:str,response:Response):
    if not verify_csrf_token(state):
        raise HTTPException(status_code=400,detail="Invalid CSRF token")
    
    token=await exchange_code_for_token(code)
    user=await get_user_profile(token)
    user_id=update_user(user,token)
    session_jwt=create_session_jwt(user_id=user_id)
    
    response=RedirectResponse(url="http://localhost:3000/dashboard")
    
    response.set_cookie(
        key="session",
        value=session_jwt,
        httponly=True,
        secure=True,
        samesite="strict"
    ) 
    
    return response 

@router.post("/logout")
def logout(response:Response):
    response.delete_cookie("session")
    
    return {"message":"Logged Out"}