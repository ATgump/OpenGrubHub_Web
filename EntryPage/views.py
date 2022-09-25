from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from .forms import UserForm,UserLoginForm,CustomerProfileForm,RestaurantProfileForm
from django.views.generic import CreateView,View
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from Profiles.models import CustomerProfile,RestaurantProfile,User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import permission_required,login_required

def username_exists(username):
    return User.objects.filter(username=username).exists()

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name: str = "login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user=True

class UserLogoutView(LogoutView):
    redirect_field_name: str = "entry_view"   

def user_entry_view(request):
    return render(request,"entry.html",{})


@login_required(redirect_field_name="EntryPage:login")
def user_landing_view(request):
    return render(request,"authenticated_user_landing.html",{})




class RestaurantCreateView(View):
    user_form_class = UserForm
    profile_form_class = RestaurantProfileForm
    #model = User
    template_name: str = "create-customer-user.html"
    success_url = reverse_lazy('authenticated_homepage')
    next_page = 'authenticated_user_landing.html'
    def get(self,request):
        user_form = self.user_form_class(prefix="UF")
        profile_form = self.profile_form_class(prefix="PF")
        return render(request,self.template_name,{'user_form':user_form,"profile_form":profile_form})
    def post(self,request):
        user_form = self.user_form_class(request.POST or None,prefix="UF")
        profile_form= self.profile_form_class(request.POST or None,prefix="PF")

        if user_form.is_valid() and profile_form.is_valid():
            ## SAVE BASE USER FORM AND SET HASHED PASSWORD
            user = user_form.save(commit=False)
            user.is_customer = False
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            ## ADD PROFILE FIELDS AND THEN SAVE PROFILE (see if can use the form_save)
            user.restaurant_profile.address = profile_form.cleaned_data.get('address')
            user.restaurant_profile.save()
            user = authenticate(request,username=username,password=password)
            if user is not None:
                print("not none")
                if user.is_active:
                    login(request,user)
                return HttpResponseRedirect(reverse('EntryPage:authenticated_homepage'))
        return render(request,self.template_name, {
            'user_form':user_form,
            'profile_form':profile_form

        })
class CustomerCreateView(View):
    user_form_class = UserForm
    profile_form_class = CustomerProfileForm
    #model = User
    template_name: str = "create-customer-user.html"
    success_url = reverse_lazy('authenticated_homepage')
    next_page = 'authenticated_user_landing.html'
    def get(self,request):
        user_form = self.user_form_class(prefix="UF")
        profile_form = self.profile_form_class(prefix="PF")
        return render(request,self.template_name,{'user_form':user_form,"profile_form":profile_form})
    def post(self,request):
        user_form = self.user_form_class(request.POST or None,prefix="UF")
        profile_form= self.profile_form_class(request.POST or None,prefix="PF")

        if user_form.is_valid() and profile_form.is_valid():
            ## SAVE BASE USER FORM AND SET HASHED PASSWORD
            user = user_form.save(commit=False)
            user.is_customer = True
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            ## ADD PROFILE FIELDS AND THEN SAVE PROFILE (see if can use the form_save)
            user.customer_profile.birth_date = profile_form.cleaned_data.get('birth_date')
            user.customer_profile.save()
            user = authenticate(request,username=username,password=password)
            if user is not None:
                print("not none")
                if user.is_active:
                    login(request,user)
                return HttpResponseRedirect(reverse('EntryPage:authenticated_homepage'))
        return render(request,self.template_name, {
            'user_form':user_form,
            'profile_form':profile_form

        })