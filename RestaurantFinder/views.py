from django.shortcuts import render
from Profiles.models import User

# Create your views here.


def home_list_view(request):
    users = User.objects.filter(is_customer=False,is_superuser=False)
    # print(users.objects)
    users= User.objects.all()
    print(users)
    for user in users:
        print("User:")
        print(user)
    context = {"users": users}
    return render(request, "RestaurantFinder/home-list-view.html", context)

    ## TO ADD FOR LOCATION STUFF
    ##users = [x for x in users if x.LOCATIONGPS < 5mi]
