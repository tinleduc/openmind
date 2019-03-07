from django.shortcuts import render
from django.views.generic import FormView, TemplateView

# Create your views here.


class homepage(TemplateView):
    template_name = 'adminpage/homepage.html'

