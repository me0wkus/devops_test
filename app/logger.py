import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path


def setup_logger(level: str, format: str, datefmt: str) -> logging.Logger:

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True, mode=0o755)

    logging.basicConfig(
        level=level.upper(),
        format=format,
        datefmt=datefmt,
        handlers=[
            RotatingFileHandler(
                mode='a',
                filename=log_dir / "app.log",
                maxBytes=10 * 1024 * 1024,
                backupCount=5,
                encoding='utf-8'
            ),
            logging.StreamHandler()
        ]
    )
    # Настройка уровня логирования для внешних библиотек
    logging.getLogger("uvicorn.access").setLevel("INFO")
    logging.getLogger("uvicorn.error").setLevel("INFO")
    return logging.getLogger(__name__)