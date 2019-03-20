"""openmind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from apps.adminpages import views as admin_views


urlpatterns = [

    path('books/', include('apps.books.urls')),
    path('admin/', admin.site.urls),
    # Homepage
    path('', admin_views.Home.as_view()),
    path('base/', admin_views.Base.as_view()),
    path('content/', admin_views.Content.as_view()),
    path('login/', admin_views.LoginView.as_view(), name='login'),

    # Content
    path('books/homosapiens/', admin_views.HomoSapiens.as_view(), name='homosapiens'),
    path('books/map/', admin_views.Map.as_view(), name='map'),


]
