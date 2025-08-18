import logging
import os

# Создаем папку для логов, если она не существует
os.makedirs('./logs', exist_ok=True)

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
