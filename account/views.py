from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('notes:note_list')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'account/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        errors = []

        if not username or not email or not password1 or not password2:
            errors.append("لطفاً همه‌ی فیلدها را پر کنید.")
        if password1 != password2:
            errors.append("رمز عبور و تکرار آن یکسان نیستند.")
        if User.objects.filter(username=username).exists():
            errors.append("این نام کاربری قبلاً استفاده شده است.")
        if User.objects.filter(email=email).exists():
            errors.append("این ایمیل قبلاً استفاده شده است.")

        if errors:
            return render(request, 'account/register.html', {
                'errors': errors,
                'username': username,
                'email': email
            })

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home')

    return render(request, 'account/register.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')