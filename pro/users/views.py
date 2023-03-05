from django.shortcuts import render, HttpResponseRedirect
from .models import User
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
# from .models import Basket
import sys
sys.path.append('C:/Users/ajsha/Desktop/backend/pro/products')
from products .models import Basket

from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:catalog'))
    else:
        form = UserLoginForm()


    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    
    baskets =  Basket.objects.filter(user=request.user)
    
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum += basket.sum()
        total_quantity += basket.quantity

    context = {
        "title" : "Store - Profile",
        "form": form,
        "baskets": baskets,
        "total_sum": total_sum,
        "total_quantity": total_quantity
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('catalog'))
