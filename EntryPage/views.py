from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from .forms import UserForm,UserLoginForm,ProfileForm
from django.views.generic import CreateView,View
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from Profiles.models import Profile
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import permission_required,login_required
# def user_login_view(request):
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username,password=password)
#         login(request.user.is_authenticated())
#     context = {
#         'form':form
#     }
#     return render(request, "login.html", context) ### directory in templates/htmldoc (or more directories presumably)

from django.contrib.auth.models import User

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


class UserCreateView(View):
    user_form_class = UserForm
    profile_form_class = ProfileForm
    #model = User
    template_name: str = "createuser.html"
    success_url = reverse_lazy('list')
    next_page = 'EntryPage:authenticated_user_landing.html'
    def get(self,request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)
        return render(request,self.template_name,{'user_form':user_form,"profile_form":profile_form})
    def post(self,request):
        user_form = self.user_form_class(request.POST)
        profile_form= self.profile_form_class(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user_profile = profile_form.save(commit=False)

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            ## profile_field = profile_form.cleaned_data["field"]
            user.set_password(password)
            user.profile = user_profile
            user.save()

            #default=1 no need to set,but this should be how to save
            #user.profile.save(role=Profile.MEMBER)
            #user.profile.save(FIELDNAME=profile_field)
            user.groups.add(1)

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                return HttpResponseRedirect(reverse('EntryPage:authenticated_homepage'))

        return render(request,self.template_name, {
            'user_form':user_form,
            'profile_form':profile_form

        })