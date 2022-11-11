from django.shortcuts import render
from django.views.generic import FormView

from .forms import ReservationForm

# Create your views here.
# def make_reservation_view(request):
#     return render(request,'ReservationApp/make-reservation.html',{})


class MakeReservationView(FormView):
    from django.urls import reverse_lazy
    template_name: str = "ReservationApp/make-reservation.html"
    reservation_form_class = ReservationForm
    success_url = reverse_lazy("RestaurantFinder:home-list-view")
    def get(self, request):
        reservation_form=self.reservation_form_class()
        return render(
            request,
            self.template_name,
            {"reservation_form": reservation_form},
        )
    def post(self, request):
        reservation_form = self.reservation_form_class(request.POST or None)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            ### ADD A RESTAURANT HERE BASED ON THE REQUEST
           
            reservation.save()
        return render(
            request,
            self.template_name,
            {"reservation_form":reservation_form,},
        )



def viewReservations(request):
    return render(request,"ReservationApp/viewReservations.html",{})
def viewSeatArea(request):
    return render(request,"ReservationApp/viewSeatArea.html",{})
def viewReservationDetail(request):
    return render(request,"ReservationApp/viewReservationDetail.html",{})
def viewContacts(request):
    return render(request,"ReservationApp/viewContacts.html",{})


def cancelReservation(request):
    return render(request,"ReservationApp/cancelReservation.html",{})
def editReservation(request):
    return render(request,"ReservationApp/editReservation.html",{})