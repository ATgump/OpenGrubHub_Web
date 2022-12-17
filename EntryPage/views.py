from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import UserForm, UserLoginForm, CustomerProfileForm, RestaurantProfileForm
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.conf import settings

## View for rendering our about us page
def aboutUsView(request):
    return render(request,"AboutUs.html")

## View for rendering our mainpage
def mainPageHFView(request):
    return render(request, "mainPage.html", {})

## View for rendering the user login page/form
class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name: str = "login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

## View for rendering the user logout view (just a redirect but for django authentication)
class UserLogoutView(LogoutView):
    redirect_field_name: str = "mainPage.html"


## View for rendering the restaurant create page
class RestaurantCreateView(View):
    user_form_class = UserForm
    profile_form_class = RestaurantProfileForm
    template_name: str = "create-restaurant-user.html"
    success_url = reverse_lazy("hf-main-page")
    next_page = "mainPage.html"
    def get(self, request):
        user_form = self.user_form_class(prefix="UF")
        profile_form = self.profile_form_class(prefix="PF")
        return render(
            request,
            self.template_name,
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "API_KEY": settings.GOOGLE_MAPS_API_KEY,
            },
        )
## Post request saves user and restaurant profile information
    def post(self, request):
        user_form = self.user_form_class(request.POST or None, prefix="UF")
        profile_form = self.profile_form_class(request.POST or None, prefix="PF")

        if user_form.is_valid() and profile_form.is_valid():
            ## SAVE BASE USER FORM AND SET HASHED PASSWORD
            user = user_form.save(commit=False)
            user.is_customer = False
            email = user_form.cleaned_data["email"]
            password = user_form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            ## ADD PROFILE FIELDS AND THEN SAVE PROFILE (see if can use the form_save)
            user.restaurant_profile.restaurant_address = profile_form.cleaned_data.get("restaurant_address")
            user.restaurant_profile.restaurant_name = profile_form.cleaned_data.get("restaurant_name")
            user.restaurant_profile.lat = profile_form.cleaned_data.get("lat")
            user.restaurant_profile.long = profile_form.cleaned_data.get("long")
            user.restaurant_profile.save()
            ## Authenticate the user
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return HttpResponseRedirect(reverse("EntryPage:hf-main-page"))
        else:
            print("FORM INVALID")
        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form,"API_KEY": settings.GOOGLE_MAPS_API_KEY,},
        )

## View for rendering the customer create page
class CustomerCreateView(View):
    user_form_class = UserForm
    profile_form_class = CustomerProfileForm
    template_name: str = "create-customer-user.html"
    success_url = reverse_lazy("hf-main-page")
    next_page = "mainPage.html"

    def get(self, request):
        user_form = self.user_form_class(prefix="UF")
        profile_form = self.profile_form_class(prefix="PF")
        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request):
        user_form = self.user_form_class(request.POST or None, prefix="UF")
        profile_form = self.profile_form_class(request.POST or None, prefix="PF")

        if user_form.is_valid() and profile_form.is_valid():
            ## SAVE BASE USER FORM AND SET HASHED PASSWORD
            user = user_form.save(commit=False)
            user.is_customer = True
            email = user_form.cleaned_data["email"]
            password = user_form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            ## ADD PROFILE FIELDS AND THEN SAVE PROFILE (see if can use the form_save)
            user.customer_profile.date_of_birth = profile_form.cleaned_data.get(
                "date_of_birth"
            )
            user.customer_profile.save()
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print("not none")
                if user.is_active:
                    login(request, user)
                return HttpResponseRedirect(reverse("EntryPage:hf-main-page"))
        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )
