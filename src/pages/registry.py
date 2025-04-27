from typing import List
import models
from nicegui import ui


@ui.refreshable
async def list_of_products() -> None:
    async def delete(product: models.Product) -> None:
        await product.delete()
        list_of_products.refresh()

    products: List[models.Product] = await models.Product.all()
    for product in reversed(products):
        with ui.card().classes("w-full"):
            with ui.row().classes("items-center w-full"):
                (
                    ui.input("Nome", on_change=product.save)
                    .bind_value(product, "name")
                    .on("blur", list_of_products.refresh)
                    .classes("flex-grow")
                )

                (
                    ui.number("Preço", on_change=product.save)
                    .bind_value(product, "price")
                    .on("blur", list_of_products.refresh)
                    .classes("w-20")
                )

                (
                    ui.number("Estoque", on_change=product.save, format="%.0f")
                    .bind_value(product, "stock")
                    .on("blur", list_of_products.refresh)
                    .classes("w-20")
                )

                (
                    ui.button(icon="delete", on_click=lambda p=product: delete(p))
                    .props("flat")
                    .classes("ml-auto")
                )


@ui.page("/registry")
async def registry():
    async def create() -> None:
        await models.Product.create(
            name=name.value, price=price.value, stock=stock.value
        )
        name.value = ""
        price.value = 0.05
        stock.value = 1
        list_of_products.refresh()

    with ui.column().classes("mx-auto w-full max-w-2xl"):
        with ui.card().classes("w-full"):
            with ui.row().classes("w-full items-center p-4 gap-4"):
                name = ui.input(label="Nome").classes("flex-grow")
                price = ui.number(label="Preço").classes("w-20")
                stock = ui.number(label="Estoque", format="%.0f").classes("w-20")
                (
                    ui.button("Adicionar", on_click=create, icon="add")
                    .props("flat")
                    .classes("ml-auto")
                )

        await list_of_products()
