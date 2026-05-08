from sqlalchemy import select
from sqlalchemy.orm import Session
from persistence.models.credit import Credit

class CreditRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, credit_id: int) -> Credit | None:
        return self.session.get(Credit, credit_id)

    def add(self, credit: Credit) -> Credit:
        self.session.add(credit)
        self.session.commit()
        self.session.refresh(credit)
        return credit

    def update(self, credit: Credit) -> Credit:
        self.session.commit()
        self.session.refresh(credit)
        return credit
    
    def merge(self, credit: Credit) -> Credit:
        self.session.merge(credit)
        self.session.commit()
        self.session.refresh(credit)
        return credit
    
    def delete(self, credit: Credit | int) -> None:
        if isinstance(credit, int):
            credit = self.get_by_id(credit)
        if credit is not None:
            self.session.delete(credit)
            self.session.commit()
    
    def get_all(self) -> list[Credit]:
        stmt = select(Credit).order_by(Credit.name.asc())        
        return list(self.session.scalars(stmt))
    
    def get_by_name_all(self, name: str | None = None) -> list[Credit]:
        stmt = select(Credit)         
        if name is not None and name.strip():
            stmt = stmt.where(Credit.name.like(f"%{name}%"))
        stmt = stmt.order_by(Credit.name.asc())
        return list(self.session.scalars(stmt))