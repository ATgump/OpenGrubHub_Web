from django.shortcuts import render
from .forms import CssCreateForm
from .models import Css
from django import forms
from django.http import HttpResponseRedirect, HttpResponseBadRequest

# Create your views here.
def cssUploadView(request):
    if request.method == "POST":
        # print(request.user) ### CAN USE THIS TO STORE IMAGES UNDER RIGHT FOLDER
        form = CssCreateForm(request.POST, request.FILES)

        if form.is_valid():
            print("---------")
            instance = Css(file=request.FILES["file"])
            instance.save()
            return HttpResponseRedirect("")
        else:
            return render(request, "FileUpload/failure.html", {"errors": form.errors})

    else:
        form = CssCreateForm()

        return render(
            request,
            "FileUpload/css_create.html",
            {
                "form": form,
            },
        )


def uploadSuccessView(request):
    return render(request, "FileUpload/success.html")
