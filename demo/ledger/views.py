import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rdbms.database import Database


# Single instance of DB for demo
db = Database()
db.create_table("merchants", columns={"id": str, "name": str, "email": str}, primary_key="id", unique_keys=["email"])
db.create_table("transactions", columns={"id": str, "merchant_id": str, "amount": str}, primary_key="id")

# Disable CSRF for simplicity
@csrf_exempt
def create_merchant(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)
    db.insert("merchants", data)
    return JsonResponse({"status": "merchant created"})

@csrf_exempt
def create_transaction(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)
    db.insert("transactions", data)
    return JsonResponse({"status": "transaction created"})

def list_transactions(request):
    transactions = db.select_all("transactions")
    return JsonResponse(transactions, safe=False)
