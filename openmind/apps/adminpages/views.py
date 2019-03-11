from django.shortcuts import render
from django.forms import ValidationError
from django.views.generic import FormView, TemplateView
from apps.adminpages.forms import LoginForm

from django.contrib.auth import authenticate, login, logout
# Create your views here.


class login(FormView):
    template_name = 'adminpage/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User authenticated
            return redirect('/home')
        return render(self.request, 'adminpage/login.html')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is None:
            form.add_error(None, ValidationError('The username or password is incorrect'))
            return self.form_valid(form)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/homepage')


class home(TemplateView):
    template_name = 'adminpage/home.html'




