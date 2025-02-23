from nicegui import app, ui

from database import init_db, close_db
from pages.registry import registry


app.on_startup(init_db)
app.on_shutdown(close_db)


@ui.page("/")
async def index():
    ui.link("Cadastro de produto", registry)


ui.run()
