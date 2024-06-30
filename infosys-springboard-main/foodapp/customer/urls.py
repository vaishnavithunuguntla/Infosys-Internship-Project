from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('add_to_cart/<int:item_id>/',views. add_to_cart, name='add_to_cart'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('update_cart_item_quantity/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
    path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('payment/success/', views.successful_payment, name='successful_payment'),
]
