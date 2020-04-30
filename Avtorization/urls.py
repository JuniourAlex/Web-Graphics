from django.urls import path
from Avtorization.views import RegisterForm

urlpatterns = [
    path('register/', RegisterForm.as_view(), name = 'register')
]