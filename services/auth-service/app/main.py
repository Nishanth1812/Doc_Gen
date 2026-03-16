from fastapi import FastAPI
from app.routers import github_oauth

app=FastAPI(title="Auth Service")

app.include_router(github_oauth.router,prefix="/auth",tags=["auth"])

@app.get("/health")
def health():
    return {
        "status":"Ok"
    }