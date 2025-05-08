import sqlite3

class Database:
    def __init__(self):
        
        self.connect = sqlite3.connect("library.db")
        self.cursor = self.connect.cursor()
        print("Database connected!")

    def create_table(self, table_name: str, columns: tuple):
        query = f"CREATE TABLE {table_name} ({columns})"
        try:
            self.cursor.execute(query)
            self.connect.commit() 
            print(f"{table_name} created successfully!")
        except sqlite3.Error as e:
            if e == "no such table":
                print(f"{table_name} does not exists!")


    def get_table(self, table: str):
        query = f"SELECT * FROM {table}"
        try: 
            self.cursor.execute(query)
            
            # return self.cursor.fetchall()
            print(self.cursor.fetchall())
        except sqlite3.Error as e:
            print(f"An error has occured: {e}")


    def insert_row(self, table: str, data: dict):
        columns = ", ".join(data.keys())
        placeholders = ", ".join((["?"] * len(data)))
        values = tuple(data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        try: 
            self.cursor.execute(query, values)
            self.connect.commit()
            print(f"Data successfully inserted in the {table}")
        except sqlite3.Error as e:
            print(f"An error has occured: {e}")
            

    def update_row(self, table: str, data_to_change: dict, condition: str):
        data_set = ", ".join([f"{column} = {value}" for column, value in data_to_change.items()])
        query = f"UPDATE {table} SET {data_set} WHERE {condition};"
        try:
            self.cursor.execute(query)
            self.connect.commit()
            print(f"Data row updated successfully!")
        except sqlite3.Error as e:
            print(f"An error has occured: {e}")


    def delete_row(self, table: str, condition: str):
        query = f"DELETE FROM {table} WHERE {condition}"
        try:
            self.cursor.execute(query)
            self.connect.commit()
            print(f"Row deleted successfully!")
        except sqlite3.Error as e:
            print(f"An error has occured: {e}")


    def search_row(self, table: str, condition: str):
        query = f"SELECT * FROM {table} WHERE {condition}"
        try:
            self.cursor.execute(query)
            self.connect.commit()
            result = self.cursor.fetchall()
            for each_row in result:
                print(result)
        except sqlite3.Error as e:
            print(f"An error has occured: {e}")


    def delete_table(self, table: str):
        query = f"DROP TABLE IF EXISTS {table}"
        try: 
            self.cursor.execute(query)
            self.connect.commit()
            print(f"{table} is deleted successfully!")
        except sqlite3.Error as e:
            print(f"An error has occured: {e}")
    
