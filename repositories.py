from sqlalchemy.orm import Session
from typing import List

from models import VendasModel


class VendasRepository:
    @staticmethod
    def find_all(db: Session) -> List[VendasModel]:
        return db.query(VendasModel).all()

    @staticmethod
    def save(db: Session, venda: VendasModel) -> VendasModel:
        if venda.id:
            db.merge(venda)
        else:
            db.add(venda)
        db.commit()
        return venda

    @staticmethod
    def find_by_id(db: Session, id: int) -> VendasModel:
        return db.query(VendasModel).filter(VendasModel.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(VendasModel).filter(VendasModel.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        venda = db.query(VendasModel).filter(VendasModel.id == id).first()
        if venda is not None:
            db.delete(venda)
            db.commit()
