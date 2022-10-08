from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import AbstractUser
from .models import CustomerProfile, RestaurantProfile, User
from django.views.generic import UpdateView

# def board_profiles_view(request):
#     return render(request,"Profiles/BoardProfiles.html",{})


@permission_required("Profiles.view_member_directory_view")
def member_directory_view(request):
    return render(request, "Profiles/MemberDirectory.html")


def customer_profile_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {"obj": obj}
    return render(
        request, "Profiles/CustomerProfile.html", context
    )  ### directory in templates/htmldoc (or more directories presumably)


def restaurant_profile_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {"obj": obj}
    return render(
        request, "Profiles/RestaurantProfile.html", context
    )  ### directory in templates/htmldoc (or more directories presumably)


class UpdateProfile(UpdateView):
    model = User
    fields = [
        "first_name",
        "last_name",
        "image",
        "url",
        "biography",
        "...",
    ]  # Keep listing whatever fields
    # the combined UserProfile and User exposes.
    template_name = "Profiles/update_profile.html"
    slug_field = "username"
    slug_url_kwarg = "slug"


# def user_list_dynamic_link(request):
#     queryset = user_profile.objects.all()
#     context = {"object_list":queryset}
#     return render(request,"user_profile/dynamic_link_view.html",context)
