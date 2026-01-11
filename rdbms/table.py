class Table:
    """
    Represents a single table with a fixed schema.
    """

    def __init__(self, name, schema, storage):
        self.name = name
        self.schema = schema          # column -> type
        self.storage = storage
        self.rows = self.storage.load(self.name)

    def insert(self, row):
        self._validate(row)
        self.rows.append(row)
        self.storage.save(self.name, self.rows)

    def select_all(self):
        return self.rows

    def _validate(self, row):
        # Ensure all schema columns exist in the row
        for column in self.schema:
            if column not in row:
                raise ValueError(f"Missing column: {column}")
