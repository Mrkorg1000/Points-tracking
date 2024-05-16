from pydantic import BaseModel


class SchemaPointBase(BaseModel):
    name: str
    alias: str

    class Config:
        orm_mode = True


class SchemaPointCreate(SchemaPointBase):
    pass


class SchemaPoint(SchemaPointBase):
    id: int