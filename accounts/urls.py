from django.urls import path
from .views import accounts_view

urlpatterns = [
    path('', accounts_view, name = "acccounts"),
]
