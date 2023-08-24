from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .utils import send_email_token
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .models import EmailVerification


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            user_profile = UserProfile.objects.create(user=user)

            email_verification = EmailVerification.objects.create(user=user)

            send_email_token(user.email)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def verify_email(request, token):
    email_verification = get_object_or_404(EmailVerification, email_token=token)
    email_verification.is_verified = True
    email_verification.save()
    
    return render(request, 'email_verified.html')




def user_login(request):
    if request.method=='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:        
        return render(request, 'login.html')    
    
def homepage(request):
    return render(request,'home.html')