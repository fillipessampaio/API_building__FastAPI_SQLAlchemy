from pydantic import BaseModel


class VendasBase(BaseModel):
    product: str
    id_seller: int
    price: float


class VendasRequest(VendasBase):
    ...


class VendasResponse(VendasBase):
    id: int

    class Config:
        orm_mode = True
