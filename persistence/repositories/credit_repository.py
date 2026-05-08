from sqlalchemy.orm import Session
from persistence.models.credit import Credit

class CreditRepository:
    def __init__(self, session:Session):
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