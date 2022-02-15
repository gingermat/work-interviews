import asyncio

import aiohttp


DATA = [
    {
        "component": "Main component 1",
        "description": "Proin viverra vel metus et faucibus. Curabitur.",
        "model": "LNA-200",
        "country": "China",
    },
    {
        "component": "Main component 2",
        "description": "Ddignissim elementum lorem.",
        "model": "KS 21",
        "country": "France",
    },
    {
        "component": "Main component 3",
        "description": "Praesent non ligula consequat, maximus est non.",
        "model": "R64",
        "country": "Guinea",
    },
    {
        "component": "Main component 4",
        "description": "Nam at nibh eget libero tincidunt lacinia.",
        "model": "Delta 7",
        "country": None,
    },
    {
        "component": "Amplifier 2",
        "description": "Aliquam leo quam, elementum et euismod eu.",
        "model": "LSA86-12.2",
        "country": "USA",
    },
    {"component": "Battery 4", "description": "Mauris metus orci.", "model": "K72", "country": "Spain"},
    {"component": "Main component6", "description": "Nulla aliquam non.", "model": "Random", "country": ""},
    {
        "component": "Main component",
        "description": "Morbi et laoreet tellus, sit amet pretium.",
        "model": "ICU",
        "country": "Bolivia",
    },
    {"component": "Main component 5", "description": "Curabitur.", "model": "RS #32", "country": "USA"},
    {
        "component": "Main component 11",
        "description": "Vivamus lacinia congue nibh sit amet aliquet.",
        "model": "N 12",
        "country": "UK",
    },
]

API_URL = "http://127.0.0.1:8080/"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(API_URL) as ws:
            for item in DATA:
                await ws.send_json(item)

            await ws.send_str("[")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
