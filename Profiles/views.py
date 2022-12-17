from django.shortcuts import render, get_object_or_404
from .models import User

## view for rendering the restaurant profiles
def restaurant_profile_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {"obj": obj}
    return render(
        request, "Profiles/RestaurantProfile.html", context
    ) 

## view for rending the restaurants management section
def restaurant_manage_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {"obj": obj}
    return render(
        request, "Profiles/manage-restaurant.html", context
    )  

