from tortoise import Tortoise


async def init_db() -> None:
    await Tortoise.init(db_url="sqlite://db/db.sqlite3", modules={"models": ["models"]})
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()
