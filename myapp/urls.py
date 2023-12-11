
# urls.py
from django.urls import path
from .views import receipt_list, receipt_detail, receipt_form, signin ,register,signout , home

urlpatterns = [
    path('receipts/', receipt_list, name='receipt-list'),
    path('receipts/<int:receipt_id>/', receipt_detail, name='receipt-detail'),
    path('receipts/new/', receipt_form, name='receipt-create'),
    path('receipts/<int:receipt_id>/edit/', receipt_form, name='receipt-edit'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('register/', register, name='register'),
    path('', home, name='home'),  
]