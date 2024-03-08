from .views import *


from django.urls import path


urlpatterns = [
    path("", ProductClass.as_view(), name="Home")
    ]