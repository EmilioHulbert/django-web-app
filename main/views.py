from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required #ensures only logged in users can visit home

# Create your views here.
def main_view(request):
    return render(request, "views/main.html", {"name": "Automax"})
@login_required #checking if user is logged in
def home_view(request):
    return render(request, "views/home.html")
    