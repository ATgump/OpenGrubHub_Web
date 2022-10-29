from django.shortcuts import render

# Create your views here.
def community_home_view(request):
    return render(request,"Community/community_home.html",{})