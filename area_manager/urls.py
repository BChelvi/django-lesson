from django.urls import path

from area_manager.views import my_test_view, hello_templated

urlpatterns = [
    path('my_test_view/', my_test_view),
    path('hello_templated/', hello_templated),
]
