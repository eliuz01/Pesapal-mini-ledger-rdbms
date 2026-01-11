from django.urls import path
from . import views

urlpatterns = [
    path("merchants", views.create_merchant),
    path("transactions", views.create_transaction),
    path("transactions/list", views.list_transactions),
]