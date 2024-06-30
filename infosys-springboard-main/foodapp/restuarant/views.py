from django.shortcuts import render, get_object_or_404
from .models import Restaurant, FoodItem

# Create your views here.
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    food_items = restaurant.food_items.all()
    image_urls = [
        "https://source.unsplash.com/random/restaurant",
        "https://source.unsplash.com/random",
        "https://source.unsplash.com/random"
    ]
    context = {
        'restaurant': restaurant,
        'image_urls': image_urls,
        'food_items': food_items
    }
    # for item in food_items:
    #     print(item.name)

    return render(request, 'restaurant_detail.html', context)