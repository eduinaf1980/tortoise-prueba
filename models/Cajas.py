from tortoise import Model, fields


class ModelCajas(Model):
    id = fields.IntField(pk=True)
    num_rastreo = fields.CharField(max_length=10, unique=True)
    descripcion = fields.CharField(max_length=150)
    peso = fields.IntField()
    precio = fields.IntField(null=True)
    coche_asig = fields.ForeignKeyField('models.ModelCoches')

    class Meta:
        table = 'cajas'