from fastapi import FastAPI
from app.routers import api_router
from app.logger import setup_logger

logger = setup_logger("debug",
                      "(%(levelname)s, %(asctime)s) => (%(name)s: %(message)s)",
                      "%Y-%m-%d %H:%M:%S")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("App is up !")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("App is down !")

app.include_router(api_router)
