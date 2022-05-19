from django.urls import path

from .views import home, redirect

urlpatterns = [
    path('', home),
    path('<str:nome>/', redirect)
]
