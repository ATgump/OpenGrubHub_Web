from django.shortcuts import render

# Create your views here.
def reservation_home_view(request):
    return render(request,'ReservationApp/home.html',{})