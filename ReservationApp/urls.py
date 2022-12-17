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

from .views import MakeReservationView,viewReservationDetail,viewReservations,editReservation,cancelReservation

app_name = "ReservationApp"
urlpatterns = [
    path("create/<int:restaurant>", MakeReservationView.as_view(), name="make-reservation-view"),
    path("<pk>/details/", viewReservationDetail, name="reservation-detail"),
    path("list/", viewReservations, name="reservation-list"),
    path("<pk>/cancel/", cancelReservation.as_view(), name="reservation-cancel"),
    path("<pk>/edit/", editReservation.as_view(), name="reservation-edit"),
]
