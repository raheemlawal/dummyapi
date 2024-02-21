import os
from supabase import create_client, Client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


load_dotenv()

url: str = os.environ["SUPAURL"]
key: str = os.environ["SUPAKEY"]
supabase: Client = create_client(url, key)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://next-frontend-1m9peb876-raheems-projects.vercel.app",
    "https://next-frontend-red.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_default():
    return "Home"

@app.get("/user/{id}")
async def get_first_user(id: int):
    response = supabase.table('User').select("*").execute()
    return response.data[id]

@app.get("/users")
async def get_all_users():
    response = supabase.table('User').select("*").execute()
    return response.data