from .table import Table
from .storage import Storage


class Database:
    """
    Coordinates tables and routes operations to them.
    """

    def __init__(self):
        self.storage = Storage()
        self.tables = {}

    def create_table(self, name, schema):
        if name in self.tables:
            raise ValueError(f"Table already exists: {name}")

        self.tables[name] = Table(name, schema, self.storage)

    def insert(self, table_name, row):
        self._get_table(table_name).insert(row)

    def select_all(self, table_name):
        return self._get_table(table_name).select_all()

    def _get_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Unknown table: {table_name}")
        return self.tables[table_name]
