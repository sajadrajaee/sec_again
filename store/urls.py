from django.urls import path
from .views import *

app_name = "store"

urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('', home, name="home")
]