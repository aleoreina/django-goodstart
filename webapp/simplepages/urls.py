from django.urls import path
from .views import home, PageView

app_name = 'simplepages'
urlpatterns = [
    path('', home, name="page-home"),
    path('<slug:slug>', PageView.as_view(), name='page-view'),
]