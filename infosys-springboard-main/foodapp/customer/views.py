from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from .models import Cart, CartItem
from restuarant.models import FoodItem
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.username = user.email  # Use email as username
            user.save()
            messages.success(request, 'User created successfully.')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'user/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def payment(request):
    cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    cart_items = cart.items.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'user/payment.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'user': request.user,
    })

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    cart_items = cart.items.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'user/cart.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def add_to_cart(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, food_item=food_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('restaurant_detail', restaurant_id=food_item.restaurant.id)

@login_required
def update_cart_item_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'status': 'success'})

@login_required
def delete_cart_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        return JsonResponse({'status': 'success'})


@login_required
def successful_payment(request):

    cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    cart_items = cart.items.all()
    total_price = sum(item.get_total_price() for item in cart_items)

    cart.is_active = False
    cart.save()

    context = {
        'user': request.user,
        'order_number': '12345678',  
        'total_price': total_price,
    }
    return render(request, 'user/successful_payment.html', context)