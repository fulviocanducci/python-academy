from connect import get_connection
from dao.daoitem import DaoItem
from models.item import Item

conn = get_connection()
try:
    dao_item = DaoItem(conn)
    #dao_item.insert("Item 101")
    print(dao_item.update("Item 101 C - Update", 101))

    result: list[Item] = dao_item.get_all()

    for row in result:
        print(row.id, "->", row.name)

except Exception as ex:
    print(ex)

finally:
    conn.close()
