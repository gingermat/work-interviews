import logging

import aiomongo
from aiohttp import web

from app.config import settings
from app.repositories import InventoryRepository
from app.views import collect_data, display_data


async def get_application():
    app = web.Application()

    log_level = logging.getLevelName(settings.LOG_LEVEL)
    logging.basicConfig(level=log_level)

    app.router.add_get("/", collect_data, allow_head=False)
    app.router.add_get("/display", display_data)

    async def on_startup(_app):
        mongo = await aiomongo.create_client(settings.MONGODB_URL)

        _app["mongo"] = mongo
        _app["inventory_repo"] = InventoryRepository(mongo, settings.INVENTORY_COLLECTION_NAME)

    async def on_shutdown(_app):
        _app["mongo"].close()
        await _app["mongo"].wait_closed()

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app
