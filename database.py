import sqlite3

class Database:
    def __init__(self):
        
        self.connect = sqlite3.connect("library.db")
        self.cursor = self.connect.cursor()
        print("Database connected!")

    def create_table(self, table_name: str, columns: tuple):
        
        query = f"CREATE TABLE {table_name} {columns}"

        self.cursor.execute(query)
        self.connect.commit() 
        print(f"{table_name} created successfully!")

        
        # try:
        #     self.cursor.execute("CREATE TABLE")
    
    def get_table(self, table: str):
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def insert_row(self, table: str, data: dict):
        columns = ", ".join(data.keys())
        placeholders = ", ".join((["?"] * len(data)))
        values = tuple(data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connect.commit()
        print(f"Data successfully inserted in the {table}")

    def update_row(self, table: str, data_to_change: dict, condition: str):
        data_set = ", ".join([f"{column} = {value}" for column, value in data_to_change.items()])
        
        query = f"UPDATE {table} SET {data_set} WHERE {condition};"
        self.cursor.execute(query)
        self.connect.commit()
        print(f"Data row updated successfully!")
    
    def delete_row(self, table: str, condition: str):
        query = f"DELETE FROM {table} WHERE {condition}"

        self.cursor.execute(query)
        self.connect.commit()
        print(f"Row deleted successfully!")
    
    def search_row(self, table: str, condition: str):
        
        query = f"SELECT * FROM {table} WHERE {condition}"


if __name__ == "__main__":
    app = Database()
    # app.create_table("books_table", "(id text, title text, author text)")
    data = {"id": "20", 
            "title": "1984", 
            "author": "George Orwell"}
    app.insert_row("books_table", data)
    # app.delete_row("books_table", "title LIKE '%Hallows'")
    # app.delete_row("books_table", "id=8")

    app.get_table("books_table")
    # app.update_row("books_table", {"id" : "5"}, "title LIKE '%Phoenix'")

    
    