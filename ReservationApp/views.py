from django.shortcuts import render
from django.views.generic import FormView

from .forms import ReservationForm

# Create your views here.
# def make_reservation_view(request):
#     return render(request,'ReservationApp/make-reservation.html',{})


class MakeReservationView(FormView):
    from django.urls import reverse_lazy

    template_name: str = "ReservationApp/make-reservation.html"
    form_class = ReservationForm
    success_url = reverse_lazy("RestaurantFinder:home-list-view")

def viewReservations(request):
    return render(request,"ReservationApp/viewReservations.html",{})
def viewSeatArea(request):
    return render(request,"ReservationApp/viewSeatArea.html",{})
def viewReservationDetail(request):
    return render(request,"ReservationApp/viewReservationDetail.html",{})