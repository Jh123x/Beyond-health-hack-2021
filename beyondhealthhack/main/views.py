from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotAllowed
from .forms import NewUserForm
from .models import ContactUsForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def index(request):
    """Home page for the website"""
    return render(request, 'home_page.html', {
        "is_authenticated": request.user.is_authenticated, 
        "username": request.user.get_username(),
    })


def user_login(request):
    """Login for the user"""
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect("/")


    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method != "POST":
        return HttpResponseNotAllowed("This method is not allowed")

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is None:
        messages.error(request, f"Incorrect username or password")
        return redirect("/login")

    login(request, user)
    messages.info(request, f"Welcome {user.get_username()}")
    return redirect("/")


def logout_view(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect('/')


def about_us(request):
    """About us page"""
    return render(request, "about_us.html")

def contact_us(request):
    """Contact us page"""
    if request.method == "GET":
        return render(request, "contact_us.html")

    if request.method != "POST":
        return HttpResponseNotAllowed("Method is not allowed")

    agree = request.POST.get("agree")
    if agree != "on":
        messages.ERROR("You have to agree to let RE:Cover to contact you")
        return redirect("/contact_us")

    name = request.POST.get("name")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone_number")
    category = request.POST.get("category")
    message = request.POST.get("message")

    try:
        form_res = ContactUsForm(name=name, email=email, phone_no=phone_number, category=category, message=message)
        form_res.save()
    except Exception:
        messages.error(request, "Invalid fields in form")
        return redirect("/contact_us")

    messages.info(request, "Form Successfully sent, we will contact you shortly")
    return redirect("/contact_us")
    

def awareness(request):
    """Awareness page"""
    return render(request, 'awareness_page.html')


@login_required
def edit_profile(request):
    """Edit profile page for the user"""
    if request.method == "GET":
        return render(request, 'profile.html')

    user = request.user
    email = request.POST.get('email', None)
    if email is not None:
        user.email = email
    
    user.save()
    messages.info(request, "Successfully added information")
    return redirect("/edit_profile")


@login_required
def payments(request):
    """Payment for the lessons"""
    return render(request, 'payment.html')


def donations(request):
    """Donations page"""
    return render(request, 'donations.html')