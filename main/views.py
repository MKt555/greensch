from django.shortcuts import render
from .models import News
from django.http import HttpResponse

# Create your views here.
def homescreen_view(request):
    print(request.headers)
    return render(request, "main/home.html", {"News":News.objects.all})#references home.html
#context is used to get some values or variables from the database

