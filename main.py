import asyncio
from tortoise import Tortoise

from models import ModelCoches, ModelCajas
from utils import run

#Esto es una prueba git
async def run_db():
    try:
        await run()
        print("Base de datos iniciada")
    except:
        print("No se inicio la base de datos")

async def migration():
        await run_db()
        #await Tortoise.generate_schemas()
        #print("Esquema generado")

        #cajas = await ModelCajas.create(num_rastreo="111112", descripcion="Mercancia de Mercadolibre", peso=5, precio=20000, coche_asig_id = 3)
        #await ModelCoches.filter(id=1).update(marca="Ferrari")
        #print(await ModelCoches.filter(id=1).first())

        conn = Tortoise.get_connection("default")

        #await conn.execute_query("INSERT INTO coches (plate, marca, modelo) VALUES ('EOP544', 'Renault', '2020')")
        await conn.execute_query("UPDATE coches SET marca='SEAT' WHERE id=1")

        c = await conn.execute_query_dict("SELECT * FROM coches WHERE id IN (SELECT DISTINCT(coche_asig_id) FROM ModelCajas)")

        print(c)

        #coches = await ModelCoches.all().values("marca", "modelo")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(migration())
    loop.close()