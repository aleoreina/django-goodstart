from django.shortcuts import render
from django.views.generic import DetailView
from .models import Page


def home(request):
    return render(request, "home.html")

class PageView(DetailView):
    model = Page
    template_name = 'page.html'