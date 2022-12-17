from django.shortcuts import render
from Profiles.models import User
from ipware import get_client_ip
from geopy.distance import geodesic
from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.


def home_list_view(request):
    ## This would be for production

    #ip, is_routable = get_client_ip(request)
    #ip_lat_lon = GeoIP2().lat_lon(ip)

    ## For now just uses my own ip

    ip_lat_lon = GeoIP2().lat_lon("71.127.165.18")

    ## Filter restaurants based on location
    users = [x for x in User.objects.filter(is_customer=False,is_superuser=False) if geodesic((x.restaurant_profile.lat,x.restaurant_profile.long),ip_lat_lon).mi < 50]

    ## Only display restuarants in a 50mi radius
    context = {"users": users}
    return render(request, "RestaurantFinder/home-list-view.html", context)

