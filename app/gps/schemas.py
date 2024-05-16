import datetime
from pydantic import BaseModel


class SchemaPointGpsBase(BaseModel):
    point_id: int
    
    lat: float
    lon: float
    speed: float

    class Config:
        orm_mode = True


class SchemaPointGpsCreate(SchemaPointGpsBase):
    pass


class SchemaPointGps(SchemaPointGpsBase):
    id: int
    time: datetime.datetime
    point_gps_id: int
