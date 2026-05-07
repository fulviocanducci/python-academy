from mysql.connector.connection import MySQLConnection
from models.item import Item

class DaoItem:
    def __init__(self, connect: MySQLConnection):
        self.connect = connect

    def get_by_id(self, item_id: int) -> Item | None:
        cursor = self.connect.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT * FROM `items` WHERE `id`=%s",
                (item_id,)
            )
            row = cursor.fetchone()
            return None if row is None else Item(row["id"], row["name"])        
        finally:
            cursor.close()

    def get_all(self) -> list[Item]:
        cursor = self.connect.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM `items` ORDER BY `id` ASC")
            rows = cursor.fetchall()
            return [Item(row["id"], row["name"]) for row in rows]
        finally:
            cursor.close()

    def get_all_by_name(self, item_name: str) -> list[Item]:
        cursor = self.connect.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT * FROM `items` WHERE `name` LIKE %s ORDER BY `name` ASC",
                (f"%{item_name}%",)
            )
            rows = cursor.fetchall()
            return [Item(row["id"], row["name"]) for row in rows]
        finally:
            cursor.close()

    def insert(self, item_name: str) -> Item:
        cursor = self.connect.cursor()
        try:
            cursor.execute(
                "INSERT INTO `items`(`name`) VALUES(%s)", 
                (item_name,)
            )
            self.connect.commit()
            item_id = cursor.lastrowid
            return Item(item_id, item_name)        
        finally:
            cursor.close()

    def update(self, item_name: str, item_id: int) -> bool:
        cursor = self.connect.cursor()
        try:            
            cursor.execute(
                "UPDATE `items` SET `name`=%s WHERE `id`=%s",
                (item_name, item_id)
            )
            self.connect.commit()    
            return cursor.rowcount > 0            
        finally:
            cursor.close()

    def delete(self, item_id: int) -> bool:
        cursor = self.connect.cursor()
        try:            
            cursor.execute(
                "DELETE FROM `items` WHERE `id`=%s",
                (item_id,)
            )
            self.connect.commit()
            return cursor.rowcount > 0            
        finally:
            cursor.close()