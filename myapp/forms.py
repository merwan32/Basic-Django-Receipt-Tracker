# forms.py
from django import forms
from .models import Receipt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class ReceiptForm(forms.ModelForm):
    """
    Form for creating and editing receipts.

    Inherits from Django's ModelForm and uses the Receipt model.

    Attributes:
        class Meta: Meta-information about the form, including the model and fields.
    """
    class Meta:
        model = Receipt
        fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']

class RegistrationForm(UserCreationForm):
    """
    Form for user registration.

    Inherits from Django's UserCreationForm, which includes fields for username, password1, and password2.

    Attributes:
        class Meta: Meta-information about the form, including the model and fields.
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']