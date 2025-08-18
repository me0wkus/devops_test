import logging
from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.models import SessionLocal, Post
from app.schemas import PostResponse, PostCreate

logger = logging.getLogger(__name__)

api_router = APIRouter(
    prefix="",
)


@api_router.get("/posts", response_model=List[PostResponse])
def read_posts():
    db: Session = SessionLocal()
    posts = db.query(Post).all()
    logger.info('Read posts')
    return posts


@api_router.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate):
    logger.info("Creating post: %s", post.title)
    db: Session = SessionLocal()
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post