"""
URL configuration for femminicidio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from femminicidioapp.views.views_utente import home, testimonianza, pannello_admin, aggiorna_stato,conferma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('testimonianza/', testimonianza, name='testimonianza'),
    path('pannello/', pannello_admin, name='pannello_admin'),
    path('conferma/', conferma, name='conferma'),
    path('pannello/aggiorna-stato/<int:pk>/', aggiorna_stato, name='aggiorna_stato'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]