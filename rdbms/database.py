from .table import Table


class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns, primary_key=None, unique_keys=None):
        if name in self.tables:
            raise ValueError("Table already exists")

        table = Table(name, columns, primary_key, unique_keys)
        self.tables[name] = table

    def insert(self, table_name, record):
        table = self.tables.get(table_name)
        if not table:
            raise ValueError("Table not found")
        table.insert(record)

    def select_all(self, table_name):
        table = self.tables.get(table_name)
        if not table:
            raise ValueError("Table not found")
        return table.select_all()

    def find_by_key(self, table_name, key, value):
        table = self.tables.get(table_name)
        if not table:
            raise ValueError("Table not found")
        return table.find_by_key(key, value)
