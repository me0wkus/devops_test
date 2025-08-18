from fastapi import FastAPI

from app.logger import setup_logger
from app.routers import api_router

logger = setup_logger("debug",
                      "(%(levelname)s, %(asctime)s) => (%(name)s: %(message)s)",
                      "%Y-%m-%d %H:%M:%S")
app = FastAPI()
logger.info("Starting server...")
app.include_router(api_router)