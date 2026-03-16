import httpx 
from app.utils.config import Settings

GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_URL = "https://api.github.com/user"

def get_authorization_url(state:str):
    return (
        f"{GITHUB_AUTH_URL}"
        f"?client_id={Settings.GITHUB_CLIENT_ID}"
        f"&redirect_uri={Settings.GITHUB_REDIRECT_URI}"
        f"&scope=repo"
        f"&state={state}") 
    
async def exchange_code_for_token(code:str):
    async with httpx.AsyncClient() as client:
        response=await client.post(
                GITHUB_TOKEN_URL,
                headers={"Accept": "application/json"},
                data={
                    "client_id": Settings.GITHUB_CLIENT_ID,
                    "client_secret": Settings.GITHUB_CLIENT_SECRET,
                    "code": code
                }
            )
        
        data=response.json()
        return data.get("access_token")

async def get_user_profile(token:str):
    async with httpx.AsyncClient() as client:
        response=await client.get(GITHUB_USER_URL,
                            headers={"Authorization":f"Bearer {token}"}
                        )
        return response.json()