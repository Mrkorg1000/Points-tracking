from app.gps.models import Gps
from app.database import async_session_maker
from sqlalchemy import select, insert


class GpsDAO:
    model = Gps

    @classmethod
    async def set_point_gps_id(cls, point_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(point_id=point_id)
            result = await session.execute(query)
            result = result.scalars().all()
            return len(result) + 1 

    @classmethod
    async def add(cls, object, point_gps_id):
        async with async_session_maker() as session:
            new_coords = cls.model(**object.dict())
            new_coords.point_gps_id = point_gps_id
            session.add(new_coords)
            await session.commit()
            return new_coords

    @classmethod
    async def get_coords(cls, point_id, offset=None, limit=None):
        async with async_session_maker() as session:
            if offset and limit:
                query = select(cls.model).filter_by(point_id = point_id).\
                    offset(offset).limit(limit)
            elif not offset and not limit:
                query = (
                    select(cls.model)
                    .filter_by(point_id=point_id)
                )
            
            result = await session.execute(query)
            point_coords_list = result.scalars().all()
            return point_coords_list
            
                
            
