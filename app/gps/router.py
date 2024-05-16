from typing import List
from fastapi import APIRouter, HTTPException, status
from app.gps.dao import GpsDAO
from app.gps.schemas import SchemaPointGpsCreate, SchemaPointGps


router = APIRouter(
    prefix="/api/v1/points/{point_id}/coords",
    tags=["Coords"],
)


@router.post("", response_model=SchemaPointGps, status_code=status.HTTP_201_CREATED)
async def create_coords(coords: SchemaPointGpsCreate):
    point_gps_id = await GpsDAO.set_point_gps_id(point_id=coords.point_id)
    new_coords = await GpsDAO.add(coords, point_gps_id)
    return new_coords


@router.get("", response_model=List[SchemaPointGps])
async def get_point_coords_list(point_id, offset=None, limit=None):
    if (offset and not limit) or (not offset and limit):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Необходимо заполнить обе графы: и 'offset' и 'limit', либо не заполнять их совсем"
        )
    coords_list = await GpsDAO.get_coords(int(point_id), offset, limit)

    if not coords_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="point not found"
        )
    return coords_list
