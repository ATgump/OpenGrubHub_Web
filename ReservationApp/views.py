from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView,UpdateView
from Profiles.models import User
from django.urls import reverse_lazy
from .models import ReservationModel
from .forms import ReservationForm

# Create your views here.
# def make_reservation_view(request):
#     return render(request,'ReservationApp/make-reservation.html',{})


class MakeReservationView(FormView):
    from django.urls import reverse_lazy
    template_name: str = "ReservationApp/make-reservation.html"
    reservation_form_class = ReservationForm
    #success_url = reverse_lazy("RestaurantFinder:home-list-view")

    def get(self, request,restaurant):
        reservation_form=self.reservation_form_class()
        return render(
            request,
            self.template_name,
            {"reservation_form": reservation_form},
        )
    def post(self, request,restaurant):
        obj = get_object_or_404(User,id=restaurant)
        reservation_form = self.reservation_form_class(request.POST or None)
        print(reservation_form.has_error)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.customer = request.user
            reservation.restaurant = obj
            reservation.save()
            return HttpResponseRedirect(obj.restaurant_profile.get_absolute_url())       
        else:
            return render(
                request,
                self.template_name,
                {"reservation_form":reservation_form},
            )



def viewReservations(request):
    if(request.user.is_customer == True):
        reservationList = [x for x in ReservationModel.objects.filter(customer=request.user)]
    else:
        reservationList = [x for x in ReservationModel.objects.filter(restaurant=request.user)]
    return render(request,"ReservationApp/viewReservations.html",{"reservationList":reservationList})

def viewSeatArea(request):
    return render(request,"ReservationApp/viewSeatArea.html",{})
def viewReservationDetail(request,pk):
    reservation = get_object_or_404(ReservationModel,id=pk)
    print(reservation)
    return render(request,"ReservationApp/viewReservationDetail.html",{"reservation":reservation})
def viewContacts(request):
    return render(request,"ReservationApp/viewContacts.html",{})



class cancelReservation(DeleteView):
    template_name = "ReservationApp/cancelReservation.html"
    model = ReservationModel
    success_url = reverse_lazy("ReservationApp:reservation-list")
    

class editReservation(UpdateView): 
    model = ReservationModel
    form_class = ReservationForm
    #template_name = "ReservationApp/make-reservation.html"
    def get_object(self, *args, **kwargs):
        reservation = get_object_or_404(ReservationModel,pk=self.kwargs["pk"])
        return reservation
    def get_success_url(self):
        return reverse_lazy("ReservationApp:reservation-list")
# def editReservation(request):
#     return render(request,"ReservationApp/editReservation.html",{})