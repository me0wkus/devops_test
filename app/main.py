from fastapi import FastAPI
from app.routers import api_router
from app.logger import logger  # Импортируем логгер

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("Приложение запущено")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Приложение остановлено")

app.include_router(api_router)
