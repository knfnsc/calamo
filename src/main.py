#!/usr/bin/env python3
from tortoise import Tortoise

from nicegui import app, ui

from registry import registry


async def init_db() -> None:
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["models"]})
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()


app.on_startup(init_db)
app.on_shutdown(close_db)

@ui.page("/")
async def index():
    ui.link("Cadastro de produto", registry)

ui.run()