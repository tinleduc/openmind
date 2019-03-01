from django.shortcuts import render
from django.template import loader
from django.views.generic import FormView, TemplateView

# Create your views here.
from django.http import HttpResponse

class index(TemplateView):
    template_name = 'books/book.html'
