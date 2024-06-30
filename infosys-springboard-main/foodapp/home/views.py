from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from restuarant.models import Restaurant

# Home page view
def index(request):
    return render(request, 'index.html')

# User dashboard view, only accessible to logged-in users
# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')


@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

# Restaurant list view based on city
def restaurant_list(request, city):
    restaurants = Restaurant.objects.filter(city__iexact=city)
    context = {
        'restaurants': restaurants,
        'city': city.capitalize()
    }
    return render(request, 'restaurant_list.html', context)
