from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Article
from app.schemas import ArticleCreate

async def create_article(db: AsyncSession, article: ArticleCreate):
    new_article = Article(**article.dict())
    
    db.add(new_article)
    
    await db.commit()
    await db.refresh(new_article)
    
    return new_article

async def get_articles(db: AsyncSession):
    result = await db.execute(select(Article))
    return result.scalars().all()

async def get_article_by_id(db: AsyncSession, article_id: int):
    result = await db.execute(select(Article).where(Article.id == article_id))
    return result.scalar_one_or_none()

async def delete_article(db: AsyncSession, article_id: int):
    article = await get_article_by_id(db, article_id)
    if article:
        await db.delete(article)
        await db.commit()
    return article