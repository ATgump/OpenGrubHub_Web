from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView,UpdateView
from Profiles.models import User
from django.urls import reverse_lazy
from .models import ReservationModel
from .forms import ReservationForm

## View to hand rendering the page for making a reservation
class MakeReservationView(FormView):
    template_name: str = "ReservationApp/make-reservation.html"
    reservation_form_class = ReservationForm

    def get(self, request,restaurant):
        reservation_form=self.reservation_form_class()
        return render(
            request,
            self.template_name,
            {"reservation_form": reservation_form},
        )

    ## post request method handles saving the reservation
    def post(self, request,restaurant):
        obj = get_object_or_404(User,id=restaurant)
        reservation_form = self.reservation_form_class(request.POST or None)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.customer = request.user ## customer is currently logged in user (only users make reservations)
            reservation.restaurant = obj ## the restaurant is the restaurant that gets passed to the request (gets it from the when prior redirect is from)
            reservation.save()
            return HttpResponseRedirect(obj.restaurant_profile.get_absolute_url())       
        else:
            return render(
                request,
                self.template_name,
                {"reservation_form":reservation_form},
            )


## View to render the reservations, if its a customer then filter the reservations that customer has made, if it's a restaurant filter the reservations made to that restaurant 
def viewReservations(request):
    if(request.user.is_customer == True):
        reservationList = [x for x in ReservationModel.objects.filter(customer=request.user)]
    else:
        reservationList = [x for x in ReservationModel.objects.filter(restaurant=request.user)]
    return render(request,"ReservationApp/viewReservations.html",{"reservationList":reservationList})


## View to render the details of a single reservation
def viewReservationDetail(request,pk):
    reservation = get_object_or_404(ReservationModel,id=pk)
    return render(request,"ReservationApp/viewReservationDetail.html",{"reservation":reservation})

## View to render the message - "are you sure you want to..."
class cancelReservation(DeleteView):
    template_name = "ReservationApp/cancelReservation.html"
    model = ReservationModel
    success_url = reverse_lazy("ReservationApp:reservation-list")
    
## View for editing a reservation    
class editReservation(UpdateView): 
    model = ReservationModel
    form_class = ReservationForm
    def get_object(self, *args, **kwargs):
        reservation = get_object_or_404(ReservationModel,pk=self.kwargs["pk"])
        return reservation
    def get_success_url(self):
        return reverse_lazy("ReservationApp:reservation-list")