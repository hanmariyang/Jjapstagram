
from django.urls import path
from user import views

urlpatterns = [
    path('signin/', views.sign_in, name='sign-in'),
]
