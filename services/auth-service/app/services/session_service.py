from shared.db.supabase import supabase
from app.services.token_encryption import encrypt_token

async def create_user(user_data,github_token):
    encrypted=encrypt_token(github_token)
    
    github_id=user_data["id"]
    
    new_user=supabase.table("users").insert({
        "github_id":github_id,
        "github_login":user_data["login"],
        "avatar_url":user_data["avatar_url"]
        "encrypted_token":encrypted["ciphertext"],
        "nonce":encrypted["nonce"]
    }).execute()
    
    return new_user.data[0]["id"]

async def update_user(user_data,github_token):
    
    encrypted=encrypt_token(github_token)
    
    github_id=user_data["id"]
    
    existing = supabase.table("users").select("*").eq("github_id", github_id).execute()
    
    if existing:
        supabase.table("users").update({
            "encrypted_token":encrypted["ciphertext"],
            "nonce":encrypted["nonce"]
        }).eq("github_id",github_id).execute()
        
        return existing.data[0]["id"]
    
    else:
        return create_user(user_data=user_data,github_token=github_id)