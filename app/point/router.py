from fastapi import APIRouter, status
from app.point.dao import PointDAO
from app.point.schemas import SchemaPoint, SchemaPointCreate


router = APIRouter(
    prefix="/api/v1/points",
    tags=["Points"],
)


@router.post("", response_model=SchemaPoint, status_code=status.HTTP_201_CREATED)
async def create_point(point: SchemaPointCreate):
    new_point = await PointDAO.add(point)
    return new_point
