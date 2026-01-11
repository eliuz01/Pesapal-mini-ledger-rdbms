from rdbms.database import Database

db = Database()

db.create_table("merchants", {
    "id": int,
    "name": str,
    "email": str
})

db.insert("merchants", {
    "id": 1,
    "name": "Eliuz Osongo",
    "email": "osongoeliuz14@gmail.com"
})

print(db.select_all("merchants"))