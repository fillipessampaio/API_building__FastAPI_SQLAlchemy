from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import VendasModel
from database import engine, Base, get_db
from repositories import VendasRepository
from schemas import VendasRequest, VendasResponse

from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/vendas", response_model=VendasResponse, status_code=status.HTTP_201_CREATED)
def create(request: VendasRequest, db: Session = Depends(get_db)):
    venda = VendasRepository.save(db, VendasModel(**request.dict()))
    return VendasResponse.from_orm(venda)


@app.get("/api/vendas", response_model=List[VendasResponse])
def find_all(db: Session = Depends(get_db)):
    vendas = VendasRepository.find_all(db)
    return [VendasResponse.from_orm(venda) for venda in vendas]


@app.get("/api/vendas/{id}", response_model=VendasResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    venda = VendasRepository.find_by_id(db, id)
    if not venda:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Venda não encontrada."
        )
    return VendasResponse.from_orm(venda)


@app.delete("/api/vendas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not VendasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Venda não encontrada."
        )
    VendasRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/api/vendas/{id}", response_model=VendasResponse)
def update(id: int, request: VendasRequest, db: Session = Depends(get_db)):
    if not VendasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Venda não encontrada."
        )
    venda = VendasRepository.save(db, VendasModel(id=id, **request.dict()))
    return VendasResponse.from_orm(venda)
