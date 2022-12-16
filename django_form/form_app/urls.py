from django.urls import path, include
from form_app import views

urlpatterns = [
    path('', views.home_view),
]
