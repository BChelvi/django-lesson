"""
URL configuration for django_lesson_project project.

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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from zoo.views import *

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'animals', AnimalViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'species', SpeciesViewSet)

admin.site.site_header = "Projet Django Lesson"

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # Urls from the area_manager app
    path('area_manager/', include('area_manager.urls')),

    # Urls from the zoo app
    path('zoo/hello/', say_hello),
    path('zoo/hello_template/', say_hello_with_template),
    path('zoo/animal_list/', animal_list),

    path('user_detail/<int:id>/', UserDetail.as_view(), name='user_detail'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('__debug__/', include(debug_toolbar.urls)),
]