from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session_maker
from app.schemas import ArticleCreate, ArticleResponse
from app.crud import create_article, get_articles, get_article_by_id, delete_article

from typing import List

router = APIRouter()

async def get_db():
    async with async_session_maker() as session:
        yield session

@router.post("/", response_model=ArticleResponse)
async def create_new_article(article: ArticleCreate, db: AsyncSession = Depends(get_db)):
    return await create_article(db, article)

@router.get("/", response_model=List[ArticleResponse])
async def list_articles(db: AsyncSession = Depends(get_db)):
    return await get_articles(db)

@router.get("/{article_id}", response_model=ArticleResponse)
async def get_article(article_id: int, db: AsyncSession = Depends(get_db)):
    article = await get_article_by_id(db, article_id)
    if not article:
        return {
            "error":"Artikel tidak ditemukan!"
        }
    return article

@router.delete("/{article_id}")
async def remove_article(article_id: int, db: AsyncSession = Depends(get_db)):
    article = await delete_article(db, article_id)
    if not article:
        return {
            "error":"Artikel tidak ditemukan!"
        }
    return {
        "message":"Artikel berhasil dihapus"
    }