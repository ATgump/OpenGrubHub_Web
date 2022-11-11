from django.shortcuts import render
from Profiles.models import User
#from geopy.distance import geodesic
#from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.


def home_list_view(request):
    ##For geoip stuff
    #users = [x for x in User.objects.filter(is_customer=False,is_superuser=False) if geodesic((x.restaurant_profile.lat,x.restaurand_profile.long),).mi < 50]
    users = User.objects.filter(is_customer=False,is_superuser=False)
    context = {"users": users}
    return render(request, "RestaurantFinder/home-list-view.html", context)

    ## TO ADD FOR LOCATION STUFF
    ##users = [x for x in users if x.LOCATIONGPS < 5mi]
