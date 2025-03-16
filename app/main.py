from fastapi import FastAPI

from app.routes.article import router as article_router
from app.database import init_db

app = FastAPI(title="API Article", version="0.1")

@app.on_event("startup")
async def on_startup():
    await init_db()
    
app.include_router(article_router, prefix="/articles", tags=["Articles"])

@app.get("/")
async def root():
    return {
        "message":"Selamat datang di project saya menggunakan FastAPI dan PostgreSQL"
    }