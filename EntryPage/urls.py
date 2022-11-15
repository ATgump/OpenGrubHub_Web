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
    CustomerCreateView,
    user_entry_view,
    UserLoginView,
    user_landing_view,
    UserLogoutView,
    RestaurantCreateView,
    get_location_post,
    createAccountHFView,
    entryPageHFView,
    mainPageHFView,
    aboutUsView,
)

app_name = "EntryPage"
urlpatterns = [
    path("for_testing", user_entry_view, name="entry_view"),
    path("aboutus/",aboutUsView,name="about-us"),
    path("create-accntHF/",createAccountHFView,name="hf-create-account"),
    path("entry-pageHF/",entryPageHFView,name="hf-entry-page"),
    path("",mainPageHFView,name="hf-main-page"),
    path("restaurant-register/post-addr/", get_location_post, name="get-location"),
    path("logout-redirect/", UserLogoutView.as_view(), name="logout"),
    path(
        "customer-register/", CustomerCreateView.as_view(), name="customer-create-view"
    ),
    path(
        "restaurant-register/",
        RestaurantCreateView.as_view(),
        name="restaurant-create-view",
    ),
    path("login/", UserLoginView.as_view(), name="login"),
    path("memberhome/", user_landing_view, name="authenticated_homepage"),
]
