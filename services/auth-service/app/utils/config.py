# Used to load Environment Variables

import os 
from dotenv import load_dotenv 

load_dotenv()

class Settings:
    GITHUB_CLIENT_ID: str=os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET: str=os.getenv("GITHUB_CLIENT_SECRET")
    GITHUB_REDIRECT_URI: str=os.getenv("GITHUB_REDIRECT_URI") 
    
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    AES_SECRET: str = os.getenv("AES_SECRET")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    CSRF_SECRET: str = os.getenv("CSRF_SECRET")
