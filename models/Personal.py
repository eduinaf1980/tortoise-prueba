from tortoise import Model, fields


class ModelPersonal(Model):
    id = fields.IntField(pk=True)
    num_document = fields.CharField(max_length=10, unique=True)
    first_name = fields.CharField(max_length=150)
    last_name = fields.CharField(max_length=200)

    class Meta:
        table = 'personal'