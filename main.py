from persistence.repositories.credit_repository import CreditRepository
from persistence.models.credit import Credit
from persistence.database.connection import SessionLocal
from datetime import datetime

session = SessionLocal()
repository = CreditRepository(session)

#credit = Credit(name = "Estudos 2", created_at = datetime.now())
#repository.add(credit)

#credit_id: int = 1;
#credit = repository.get_by_id(credit_id)
#if credit is not None:
#    credit.created_at = datetime.now()
#    repository.update(credit)

result = repository.get_by_name_all("")
for credit in result:
    print(credit.id, credit.name, credit.created_at)