from sqlmodel import SQLModel
from datetime import datetime

class ArticleBase(SQLModel):
    title: str
    content: str
    
class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int
    created_at: datetime