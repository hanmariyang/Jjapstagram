
from django.urls import path
from content import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
