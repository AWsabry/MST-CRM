from django.shortcuts import render

# Create your views here.


def organizations_home(request):
    return render(request, "organizations_home.html")