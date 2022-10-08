"""rnd_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    member_directory_view,
    customer_profile_view,
    UpdateProfile,
    restaurant_profile_view,
)

app_name = "Profiles"
urlpatterns = [
    path("", member_directory_view, name="member_directory_view"),
    path("customer/<int:id>", customer_profile_view, name="CustomerProfile"),
    path("restaurant/<int:id>", restaurant_profile_view, name="RestaurantProfile"),
    path("<user>/edit", UpdateProfile.as_view(), name="edit_profile"),
]
