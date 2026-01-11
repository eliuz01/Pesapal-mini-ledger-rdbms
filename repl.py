from rdbms.database import Database

db = Database()

print("Welcome to Mini-Ledger RDBMS REPL")
print("Commands: CREATE, INSERT, SELECT, FIND, EXIT\n")

while True:
    try:
        cmd = input("db> ").strip()
        if not cmd:
            continue

        if cmd.upper() == "EXIT":
            print("Goodbye!")
            break

        # CREATE TABLE table_name col1,col2,... PRIMARY=key UNIQUE=col
        if cmd.upper().startswith("CREATE"):
            parts = cmd.split()
            table_name = parts[2]
            columns_part = parts[3].split(",")
            columns = {col: str for col in columns_part}  # simple: all str
            primary_key = None
            unique_keys = []

            # Optional PRIMARY=col UNIQUE=col1,col2
            for part in parts[4:]:
                if part.upper().startswith("PRIMARY="):
                    primary_key = part.split("=")[1]
                if part.upper().startswith("UNIQUE="):
                    unique_keys = part.split("=")[1].split(",")

            db.create_table(table_name, columns, primary_key, unique_keys)
            print(f"Table '{table_name}' created.")

        # INSERT INTO table_name key1=value1,key2=value2
        elif cmd.upper().startswith("INSERT"):
            parts = cmd.split()
            table_name = parts[2]
            kv_pairs = parts[3].split(",")
            record = {}
            for kv in kv_pairs:
                k, v = kv.split("=")
                record[k] = v
            db.insert(table_name, record)
            print("Row inserted.")

        # SELECT * FROM table_name
        elif cmd.upper().startswith("SELECT"):
            table_name = cmd.split()[-1]
            rows = db.select_all(table_name)
            for row in rows:
                print(row)

        # FIND table_name column=value
        elif cmd.upper().startswith("FIND"):
            parts = cmd.split()
            table_name = parts[1]
            column, value = parts[2].split("=")
            row = db.find_by_key(table_name, column, value)
            print(row)

        else:
            print("Unknown command.")

    except Exception as e:
        print("Error:", e)