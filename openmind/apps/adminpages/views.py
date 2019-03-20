from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.views.generic import FormView, TemplateView
from apps.adminpages.forms import LoginForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.


# class LoginView(FormView):
#     template_name = 'adminpages/login.html'
#     form_class = LoginForm
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             # User authenticated
#             return redirect('/books')
#         return render(self.request, 'adminpages/login.html')
#
#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         user = authenticate(self.request, email=email, password=password)
#
#         if user is None:
#             form.add_error(None, ValidationError('The username or password is incorrect'))
#             return self.form_valid(form)
#
#         login(self.request, user)
#         # Redirect to a success page
#
#         return redirect('/books')
#
#
# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
#     return redirect('/homepage')


class LoginView(FormView):
    template_name = 'adminpage/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User authenticated
            return redirect('/books')
        return render(self.request, 'adminpages/login.html')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is None:
            form.add_error(None, ValidationError('The username or password is incorrect'))
            return self.form_invalid(form)

        login(self.request, user)
        # Redirect to a success page.
        return redirect('/books')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/login')


class Home(TemplateView):
    template_name = 'adminpages/home.html'


class Base(TemplateView):
    template_name = 'adminpages/base.html'


class Content(TemplateView):
    template_name = 'adminpages/basecontent.html'


class HomoSapiens(TemplateView):
    template_name = 'books/homosapiens.html'


class Map(TemplateView):
    template_name = 'adminpages/map.html'


