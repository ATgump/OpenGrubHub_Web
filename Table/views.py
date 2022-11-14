from django.shortcuts import render
# from .forms import 
# class CustomerCreateView(View):
#     user_form_class = UserForm
#     profile_form_class = CustomerProfileForm
#     template_name: str = "create-customer-user.html"
#     success_url = reverse_lazy("authenticated_homepage")
#     next_page = "authenticated_user_landing.html"

#     def get(self, request):
#         user_form = self.user_form_class(prefix="UF")
#         profile_form = self.profile_form_class(prefix="PF")
#         return render(
#             request,
#             self.template_name,
#             {"user_form": user_form, "profile_form": profile_form},
#         )

#     def post(self, request):
#         user_form = self.user_form_class(request.POST or None, prefix="UF")
#         profile_form = self.profile_form_class(request.POST or None, prefix="PF")

#         if user_form.is_valid() and profile_form.is_valid():
#             ## SAVE BASE USER FORM AND SET HASHED PASSWORD
#             user = user_form.save(commit=False)
#             user.is_customer = True
#             email = user_form.cleaned_data["email"]
#             password = user_form.cleaned_data["password"]
#             user.set_password(password)
#             user.save()
#             ## ADD PROFILE FIELDS AND THEN SAVE PROFILE (see if can use the form_save)
#             user.customer_profile.date_of_birth = profile_form.cleaned_data.get(
#                 "date_of_birth"
#             )
#             user.customer_profile.save()
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 print("not none")
#                 if user.is_active:
#                     login(request, user)
#                 return HttpResponseRedirect(reverse("EntryPage:authenticated_homepage"))
#         return render(
#             request,
#             self.template_name,
#             {"user_form": user_form, "profile_form": profile_form},
#        )
