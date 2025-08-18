# Sample of CI/CD (Docker usage)
Status of last deployment:<br> 
<img src="https://github.com/me0wkus/devops_test/workflows/CI/CD/badge.svg?branch=main"><br>

**Как запускается процесс развёртывания:**
- Процесс развёртывания приложения и базы данных начинается при ``git push`` в главную ветку ``main``.

**Секреты, которые нужно указать:**
- SSH_PRIVITE_KEY - Приватный ключ SSH
- SSH_USERNAME - Имя пользователя (*часто root*)
- SSH_HOST - Адрес сервера
- DOCKER_USERNAME - Имя пользователя Docker Hub
- DOCKER_PASSWORD - Пароль Docker Hub
- DOCKERHUB_NAMESPACE - Имя создателя репозитория
- DOCKERHUB_REP - Название репозитория
- COMPOSE - Путь до файла docker-compose.yml, например - ``https://raw.githubusercontent.com/user/repo/branch/path/to/file``

**Как запустить локально на UNIX:**
- Склонировать репозиторий - ``git clone git@github.com:me0wkus/devops_test.git``
- Установить Docker и Docker-Compose: 
``apt update && apt upgrade -y``
``apt install docker.io``
``apt install docker-compose``
- Перейти в склонированный репозиторий - ``cd ./path``
- Запустить - ``docker-compose up``
- Чтобы остановить процессы - ``docker-compose down``
### Технологии:

- **Язык программирования**: Python
- **Веб-фреймворк**: FastAPI
- **База данных**: PostgreSQL
- **ORM**: SQLAlchemy
- **Контейнеризация**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Сервер**: Uvicorn