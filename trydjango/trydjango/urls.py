"""trydjango URL Configuration

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
from django.contrib.auth import views as auth_views

from pages.views import hjem_view, members_view, kontakt_oss_view, om_oss_view

urlpatterns = [
    path('', hjem_view, name="lhbk-hjem"),
    path('hjem/', hjem_view, name="hjem-hjem"),
    path('kontakt_oss/', kontakt_oss_view, name="kontakt-oss"),
    path('om_oss/', om_oss_view, name="om-oss"),
    path('medlemmer/', members_view, name="medlemmer"),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')

    

]
