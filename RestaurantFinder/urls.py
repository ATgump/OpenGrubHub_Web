from django.urls import path

from .views import home_list_view

app_name = "RestaurantFinder"
urlpatterns = [
    path("", home_list_view, name="home-list-view")
]
