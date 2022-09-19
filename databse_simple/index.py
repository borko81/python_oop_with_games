import sqlite3

sql = """
        CREATE TABLE IF NOT EXISTS person (
            id integer PRIMARY KEY,
            name text NOT NULL
        )
        """

sql_insert = """
    INSERT INTO person(id, name) VALUES(?, ?)
"""


class OpenConnection:

    def __init__(self, db_name: str):
        self.name = db_name
        self.con = self.open_connect()

    def open_connect(self):
        try:
            con = sqlite3.connect(self.name)
        except Exception as e:
            print(e)
            return None
        else:
            return con


class CreateTable:

    def __init__(self, name, query, con: OpenConnection):
        self.name = name
        self.query = query
        self.con = con

    def create_table(self):
        con = self.con.open_connect()
        if con is not None:
            cur = con.cursor()
            cur.execute(self.query)
            con.close()


class InsertNewRecords:

    def __init__(self, con: OpenConnection, query, args):
        self.query = query
        self.params = args
        self.con = con.open_connect()

    def insert_new_record(self):
        if self.con is not None:
            cur = self.con.cursor()
            print(self.params)
            try:
                cur.execute(self.query, self.params)
                self.con.commit()
                self.con.close()
            except Exception as e:
                print(e)
            else:
                print('Insert 1 records')


if __name__ == '__main__':
    o = OpenConnection('mydb.db')
    c = CreateTable('person', sql, o)
    c.create_table()
    i = InsertNewRecords(o, sql_insert, (1, 'Borko'))
    i.insert_new_record()
