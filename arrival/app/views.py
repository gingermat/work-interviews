import logging

import aiohttp
from aiohttp import WSMessage, web

from app.config import settings
from app.models import InventoryModel, ModelException


logger = logging.getLogger(__name__)


async def collect_data(request: web.Request) -> web.WebSocketResponse:
    """Receive data from websocket"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:  # type: WSMessage

        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == "close":
                await ws.close()
        elif msg.type == aiohttp.WSMsgType.ERROR:
            logger.info("Websocket connection close with error: %s", ws.exception())

        try:
            item = InventoryModel.from_json(msg.data)
            await request.app["inventory_repo"].insert(item)
        except ModelException as exc:
            logger.error(exc)

    logger.debug("Websocket connection closed")

    return ws


async def display_data(request: web.Request) -> web.Response:
    """Display data with pagination"""
    try:
        page = int(request.query.get("page", 1))
    except ValueError:
        page = 1

    page = max(page, 1)
    offset = (page - 1) * settings.INVENTORY_ITEMS_PER_PAGE

    logger.debug("Offset - %d", offset)

    items = await request.app["inventory_repo"].fetch_many({}, offset, settings.INVENTORY_ITEMS_PER_PAGE)

    if not items:
        raise web.HTTPNotFound

    return web.json_response([item.to_dict() for item in items])
