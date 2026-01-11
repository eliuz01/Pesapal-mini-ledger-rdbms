# Pesapal-mini-ledger-rdbms
I implemented a minimal relational database management system (RDBMS) from scratch. I demonstrated using a small Django backend. Thus, it depicts a simplified transaction ledger similar to components used in payment processing systems.

## The deliverables or problem Statement
The following features will be supported:

- Table creation with basic data types
- CRUD operations
- Primary and unique keys
- Basic indexing
- Simple joins
- A SQL-like interface with an interactive REPL

NB: The database engine is  used directly (without ORM) by a small Django web app to demonstrate real-world usage through CRUD operations.

## Project Structure
Pesapal-mini-ledger-rdbms/
├── 🟡 🚫 **.gitignore**
├── 📂 data/
│   └── ⚙️ merchants.json
├── 📂 demo/
│   ├── 📄 db.sqlite3
│   ├── 📂 demo/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 asgi.py
│   │   ├── 📄 settings.py
│   │   ├── 📄 urls.py
│   │   └── 📄 wsgi.py
│   ├── 📂 ledger/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 admin.py
│   │   ├── 📄 apps.py
│   │   ├── 📂 migrations/
│   │   │   └── 📄 __init__.py
│   │   ├── 📄 models.py
│   │   ├── 📄 tests.py
│   │   ├── 📄 urls.py
│   │   └── 📄 views.py
│   └── 📄 manage.py
├── 📄 project_structure.text
├── 📂 rdbms/
│   ├── 📄 __init__.py
│   ├── 📂 data/
│   ├── 📄 database.py
│   ├── 📄 storage.py
│   └── 📄 table.py
├── 🔴 📖 **README.md**

## Data Model (ERD)

- The ERD for this project can be found in the [documentation folder] 
https://github.com/eliuz01/Pesapal-mini-ledger-rdbms/main/documentation/ERD.drawio.png
## RDBMS Features Implemented 
- In-memory table storage with optional file persistence
- Schema enforcement
- Primary key and unique key constraints
- Dictionary-based indexing for fast lookups
- Insert and select operations
- Indexed key-based queries
- Modular design (Database, Table, Storage)

## Interactive REPL
I included an interactive REPL with SQL-like commands 
Supported commands include;

- CREATE TABLE merchants id,name,email PRIMARY=id UNIQUE=email
- INSERT INTO merchants id=1,name=Pesapal,email=store@pesapal.com
- SELECT * FROM merchants
- FIND merchants email=store@pesapal.com
- EXIT

The commands show table creation, insertion, full table scans, and indexed lookups.

## Django Demo (with no ORM)
I included a small backend that demonstrates integration with the custom RDBMS.

The Key Rules Followed included: 
- One Django app
- No Django ORM
- Uses the custom database engine directly
- Minimal scope, proof of integration only

## Endpoints 
| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| POST   | `/merchants`         | Create a merchant     |
| POST   | `/transactions`      | Create a transaction  |
| GET    | `/transactions/list` | List all transactions |


## Running the Django Demo
# First, start the server
- cd demo
- python manage.py runserver

# Create a merchant
- curl -X POST http://127.0.0.1:8000/merchants \
- -H "Content-Type: application/json" \
- -d '{"id":"1","name":"Eliuz","email":"osongoeliuz14@.com"}'

# Create Transaction 
- curl -X POST http://127.0.0.1:8000/transactions \
- -H "Content-Type: application/json" \
- -d '{"id":"tx1","merchant_id":"1","amount":"100"}'

# List Transaction 
- curl http://127.0.0.1:8000/transactions/list
