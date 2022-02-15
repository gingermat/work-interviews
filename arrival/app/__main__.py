from aiohttp import web

from app.config import settings
from app.server import get_application


if __name__ == "__main__":
    web.run_app(get_application(), host=settings.API_HOST, port=settings.API_PORT)
