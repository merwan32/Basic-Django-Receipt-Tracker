# tests.py
from django.test import TestCase,Client
from django.contrib.auth.models import User
from .models import Receipt
from django.urls import reverse

# Create your tests here.


class ReceiptModelTest(TestCase):

    def setUp(self):
        # Arrange: Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_receipt_creation(self):
        # Arrange: Create a test receipt
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Test item 1, Test item 2',
            total_amount=50.00
        )

        # Assert: Verify the created receipt
        self.assertEqual(receipt.store_name, 'Test Store')
        self.assertEqual(receipt.user, self.user)



class ReceiptViewTest(TestCase):

    def setUp(self):
        # Arrange: Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Arrange: Create a test receipt
        self.receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Test item 1, Test item 2',
            total_amount=50.00
        )

    def test_receipt_list_view(self):
        # Arrange: Create a test client and login
        client = Client()
        client.login(username='testuser', password='testpassword')

        # Act: Make a GET request to the receipt-list view
        response = client.get(reverse('receipt-list'))

        # Assert: Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Store')  # Check if store name is in the response content

    def test_home_view(self):
        # Arrange: Create a test client

        client = Client()

        # Act: Make a GET request to the home view
        response = client.get(reverse('home'))

        # Assert: Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Basic Django Receipt Tracker',html=True)
