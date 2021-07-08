from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotAllowed
from .forms import NewUserForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def index(request):
    """Home page for the website"""
    return render(request, 'main_page.html', {
        "is_authenticated": request.user.is_authenticated, 
        "username": request.user.get_username(),
    })


def register(request):
    """Register to be a user"""
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect("/")
    
    form = NewUserForm()
    if request.method == "GET":
        return render(request, 'register.html', {"register_form": form})

    if request.method != "POST":
        return HttpResponseNotAllowed("Only GET and POST methods are allowed")

    submitted_form = NewUserForm(request.POST)
    if not submitted_form.is_valid():
        all_errors = submitted_form.errors.items()
        acc = []
        for field, errors in all_errors:
            for error in errors:
                acc.append(f"{field}: {error}\n")
        messages.error(request, f"Invalid registration:\n{''.join(acc)}")
        return redirect('/register')

    user = submitted_form.save()
    login(request, user)
    messages.success(request, "Successful registration")
    return redirect("/")


def user_login(request):
    """Login for the user"""
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect("/")

    form = AuthenticationForm()
    if request.method == "GET":
        return render(request, 'login.html', {'login_form': form})
    
    if request.method != "POST":
        return HttpResponseNotAllowed("This method is not allowed")

    login_form = AuthenticationForm(request, request.POST)

    if not login_form.is_valid():
        all_errors = login_form.errors.items()
        acc = []
        for _, errors in all_errors:
            for error in errors:
                acc.append(f"{error}\n")
        messages.error(request, f"Invalid login {''.join(acc)}")
        return redirect('/login')

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)

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
    return render(request, "contact_us.html")


@login_required
def edit_profile(request):
    """Edir profile page for the user"""
    if request.method == "GET":
        return render(request, 'profile.html')

    user = request.user
    email = request.POST.get('email', None)
    if email is not None:
        user.email = email
    
    user.save()
    messages.info(request, "Successfully added information")
    return redirect("/edit_profile")

    

