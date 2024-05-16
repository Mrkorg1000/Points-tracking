from sqlalchemy import DateTime, Float, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime


class Gps(Base):
    __tablename__ = "gps"

    id = Column(Integer, primary_key=True)
    point_id = Column(
        Integer,
        ForeignKey(
            "points.id"
        ),
        nullable=False,
    )
    point = relationship("Point", back_populates="gps")
    point_gps_id = Column(Integer, nullable=False, default=0)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    time = Column(DateTime, default=lambda: datetime.datetime.now(), nullable=False)
