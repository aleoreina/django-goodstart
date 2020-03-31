from django.views.generic.base import TemplateView

class LoginView(TemplateView):

    template_name = "users/login.html"

class RegisterView(TemplateView):

    template_name = "users/register.html"
