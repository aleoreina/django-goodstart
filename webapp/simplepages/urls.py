from django.urls import path
from .views import home

app_name = 'simplepages'
urlpatterns = [
    path('', home, name="simplepages-home"),
]