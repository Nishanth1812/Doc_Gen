from jose import jwt
import time
from app.utils.config import Settings

ALGORITHM = "HS256"


def create_session_jwt(user_id: str) -> str:
    now = int(time.time())
    payload = {
        "sub": user_id,
        "iat": now,
        "exp": now + 86400,  # 1 day
    }

    return jwt.encode(payload, Settings.JWT_SECRET, algorithm=ALGORITHM)