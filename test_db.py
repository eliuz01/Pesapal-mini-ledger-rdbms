from rdbms.database import Database

db = Database()

db.create_table(
    "merchants",
    columns={"id": int, "name": str, "email": str},
    primary_key="id",
    unique_keys=["email"]
)

db.insert("merchants", {
    "id": 1,
    "name": "Pesapal Store",
    "email": "store@pesapal.com"
})

print(db.select_all("merchants"))
print(db.find_by_key("merchants", "email", "store@pesapal.com"))
