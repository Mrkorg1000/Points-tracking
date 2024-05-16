from app.point.models import Point
from app.database import async_session_maker


class PointDAO:
    model = Point

    @classmethod
    async def add(cls, object):
        async with async_session_maker() as session:
            new_object = cls.model(**object.dict())
            session.add(new_object)
            await session.commit()
            return new_object
