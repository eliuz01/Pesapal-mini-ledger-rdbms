class Table:
    def __init__(self, name, columns, primary_key=None, unique_keys=None):
        self.name = name
        self.columns = columns
        self.primary_key = primary_key
        self.unique_keys = unique_keys or []

        self.rows = []
        self.indexes = {}

        if primary_key:
            self.indexes[primary_key] = {}

        for key in self.unique_keys:
            self.indexes[key] = {}

    def insert(self, record):
        # Basic schema check
        for column in self.columns:
            if column not in record:
                raise ValueError(f"Missing column: {column}")

        # Enforce primary and unique keys
        for key, index in self.indexes.items():
            value = record[key]
            if value in index:
                raise ValueError(f"Duplicate value for key: {key}")

        self.rows.append(record)

        # Update indexes
        for key, index in self.indexes.items():
            index[record[key]] = record

    def select_all(self):
        return self.rows

    def find_by_key(self, key, value):
        if key not in self.indexes:
            raise ValueError(f"No index on column: {key}")
        return self.indexes[key].get(value)
