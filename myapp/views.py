# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt
from .forms import ReceiptForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login ,logout

# Create your views here.


@login_required
def receipt_list(request):
    """
    View to display a list of receipts submitted by the logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response object.
    """
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipt_list.html', {'receipts': receipts})


@login_required
def receipt_detail(request, receipt_id):
    """
    View to show detailed information about a specific receipt.

    Args:
        request (HttpRequest): The HTTP request object.
        receipt_id (int): The ID of the receipt to display.

    Returns:
        HttpResponse: The response object.
    """
    receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    return render(request, 'receipt_detail.html', {'receipt': receipt})



@login_required
def receipt_form(request, receipt_id=None):
    """
    View to submit new receipts and edit existing ones.

    Args:
        request (HttpRequest): The HTTP request object.
        receipt_id (int, optional): The ID of the receipt to edit. Defaults to None.

    Returns:
        HttpResponse: The response object.
    """
    if receipt_id:
        receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    else:
        receipt = None

    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt-list')
    else:
        form = ReceiptForm(instance=receipt)

    return render(request, 'receipt_form.html', {'form': form})



def signin(request):
    """
    View for custom user sign-in.

    Handles the sign-in process, authenticating the user and redirecting to a specified URL upon success.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        # Create an AuthenticationForm instance with the submitted POST data
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            # Extract username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the authenticated user
                login(request,user)
                return redirect('receipt-list') 
    else:
        # For GET requests, create a new empty AuthenticationForm instance
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def signout(request):
    """
    View for custom user logout.

    Logs out the user and redirects to a specified URL.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response object.
    """
    logout(request)
    return redirect('home')

def register(request):
    """
    View for custom user registration.

    Handles the user registration process and logs in the user upon successful registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            
            # Log in the new user
            login(user)
            return redirect('your_register_redirect_url')  # Replace with the actual URL
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})



def home(request):
    """
    Home view.

    Renders the main page of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, 'home.html')