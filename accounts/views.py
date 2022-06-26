from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html')
