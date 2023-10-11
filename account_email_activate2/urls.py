"""
URL configuration for account_email_activate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from auth_app.views import UserAPI, Activate
from crud_app.views import ProjectAPI, ProjectDetailsAPI
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", UserAPI.as_view()),
    path("access/", token_obtain_pair),
    path("refresh", token_refresh),
    path("activate/<uidb64>/<token>/", Activate.as_view(), name="activate"),
    path("project/", ProjectAPI.as_view()),
    path("project_details/<int:pk>/", ProjectDetailsAPI.as_view())

]
