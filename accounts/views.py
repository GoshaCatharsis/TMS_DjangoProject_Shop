from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegistrationForm


class Registration(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)






