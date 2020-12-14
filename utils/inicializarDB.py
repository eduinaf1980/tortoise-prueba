from tortoise import Tortoise

async def run(generate_schemas=False):
    await Tortoise.init(
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": "pruebastortoise",
                        "host": "localhost",
                        "password": "Andf1980",
                        "port": 5432,
                        "user": "postgres"
                    }
                }
            },
            "apps": {
                "models": {
                    "models": ["models"],
                    "default_connection": "default",
                }
            },
        }
    )
    if generate_schemas:
        await Tortoise.generate_schemas()