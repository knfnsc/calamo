from tortoise import fields, models


class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=11, decimal_places=2)
    stock = fields.IntField()
