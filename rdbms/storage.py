import json
import os


class Storage:
    """
    Simple file-based storage engine.

    Responsibilities:
    - Persist table data to disk
    - Load table data into memory
    - Abstract file I/O away from the database logic

    Data is stored as JSON files, one per table.
    """

    def __init__(self, data_dir="data"):
        # Directory where table files are stored
        self.data_dir = data_dir

        # Ensure the data directory exists
        os.makedirs(self.data_dir, exist_ok=True)

    def _path(self, table_name):
        """
        Build the file path for a given table.
        """
        return os.path.join(self.data_dir, f"{table_name}.json")

    def load(self, table_name):
        """
        Load all rows for a table from disk.

        Returns an empty list if the table has no persisted data yet.
        """
        path = self._path(table_name)
        if not os.path.exists(path):
            return []

        with open(path, "r") as f:
            return json.load(f)

    def save(self, table_name, rows):
        """
        Persist all rows for a table to disk.
        This overwrites the existing file.
        """
        with open(self._path(table_name), "w") as f:
            json.dump(rows, f, indent=2)
