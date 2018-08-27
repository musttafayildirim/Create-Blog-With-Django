from django.shortcuts import render,redirect
from .forms import LoginForm , SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})




def loginUser(request):
    
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.warning(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"users/login.html",context)

        messages.success(request,"Başarıyla giriş yaptınız.")
        login(request,user)
        return redirect("index")

    return render(request,"users/login.html",context)


def logoutUser(request):
    logout(request)
    messages.info(request,"Çıkış yapıldı.")
    return redirect("index")



