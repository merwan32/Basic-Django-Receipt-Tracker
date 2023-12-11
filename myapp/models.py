# models.py
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Receipt(models.Model):
    """
    Model representing a receipt.

    Attributes:
        store_name (str): The name of the store where the purchase was made.
        date_of_purchase (Date): The date when the purchase was made.
        item_list (str): A simple text field containing the list of items purchased.
        total_amount (Decimal): The total amount of the purchase.
        user (ForeignKey): Links the receipt to a Django User.
    """

    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receipt #{self.id} - {self.store_name}"