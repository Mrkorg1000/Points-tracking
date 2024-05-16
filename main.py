from fastapi import FastAPI
from app.point.router import router as router_points
from app.gps.router import router as router_gps
from app.database import engine, Base

app = FastAPI()

app.include_router(router_points)
app.include_router(router_gps)


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
