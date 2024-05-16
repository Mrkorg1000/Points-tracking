from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from app.database import Base



class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    alias = Column(String, nullable=False)
    gps = relationship("Gps", back_populates="point")
