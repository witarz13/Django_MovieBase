"""
URL configuration for movies project.

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
from movies import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.movies),
    path('<int:id>', view.detail),
    path('add',view.add),
    path('delete/<int:id>',view.delete),
    path('database',view.database),
    path('filterd',view.filtered),
    path('sign',view.sign),
    path('login',view.login)
]
