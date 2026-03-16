# Role Based access token helpers

from jose import jwt 
from datetime import datetime,timedelta,UTC
from app.utils.config import Settings 

ALGORITHM="HS256"

def create_csrf_token():
    payload={"iat":datetime.now(UTC),"exp":datetime.now(UTC) + timedelta(minutes=30)}
    
    return jwt.encode(payload,Settings.CSRF_SECRET,algorithm=ALGORITHM)

def verify_csrf_token(token:str):
    try:
        jwt.decode(token,Settings.CSRF_SECRET,algorithms=[ALGORITHM])
        return True
    except Exception:
        return False
    

def create_session_jwt(user_id:str):
    payload={
        "sub":user_id,
        "iat":datetime.now(UTC),
        "exp":datetime.now(UTC)+timedelta(days=1),
    } 
    
    return jwt.encode(payload,Settings.JWT_SECRET,algorithm=ALGORITHM)