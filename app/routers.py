from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.models import SessionLocal, Post
from app.schemas import PostResponse, PostCreate
from app.logger import logger

api_router = APIRouter(
    prefix="",
)


@api_router.get("/posts", response_model=List[PostResponse])
def read_posts():
    db: Session = SessionLocal()
    posts = db.query(Post).all()
    logger.info("Got all posts")
    return posts


@api_router.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate):
    logger.info("Creating post: %s", post.title)
    db: Session = SessionLocal()
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    logger.info("Post created with ID: %d", db_post.id)
    return db_post
