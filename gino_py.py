import asyncio
from gino import Gino

db = Gino()

url = 'postgresql://postgres:artick@localhost:5432/gino'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')


async def connect_db():
    await db.set_bind(url)
    await db.gino.create_all()
    await db.pop_bind().close()


async def select_all():
    await db.set_bind(url)
    users = await User.query.gino.all()

asyncio.get_event_loop().run_until_complete(select_all())
