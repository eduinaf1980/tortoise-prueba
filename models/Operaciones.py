from tortoise import Model, fields


class ModelOperaciones(Model):
    id = fields.IntField(pk=True)
    descripcion = fields.CharField(max_length=200)
    fecha = fields.DateField()
    entrega = fields.DatetimeField(auto_now_add=True)
    observaciones = fields.CharField(max_length=300)
    personal = fields.ForeignKeyField('models.ModelPersonal')
    coche = fields.ForeignKeyField('models.ModelCoches')

    class Meta:
        table = 'operaciones'