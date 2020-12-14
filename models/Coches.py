from tortoise import Model, fields


class ModelCoches(Model):
    id = fields.IntField(pk=True)
    plate = fields.CharField(max_length=10, unique=True)
    marca = fields.CharField(max_length=150)
    modelo = fields.CharField(max_length=6)

    class Meta:
        table = 'coches'