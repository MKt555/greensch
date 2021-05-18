from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def academyscreen_view(request):
    print(request.headers)
    return render(request, "academy/academy.html", {})#references home.html
#context is used to get some values or variables from the database