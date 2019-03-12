from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.views.generic import FormView, TemplateView
from apps.adminpages.forms import LoginForm

from django.contrib.auth import authenticate, login, logout
# Create your views here.


class LoginForm(FormView):
    template_name = 'adminpages/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User authenticated
            return redirect('/home')
        return render(self.request, 'adminpages/login.html')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is None:
            form.add_error(None, ValidationError('The username or password is incorrect'))
            return self.form_valid(form)

        login(self.request, user)
        # Redirect to a success page

        return redirect('/home')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/homepage')


class Home(TemplateView):
    template_name = 'adminpages/home.html'


class HomoSapiens(TemplateView):
    template_name = 'books/homosapiens.html'



