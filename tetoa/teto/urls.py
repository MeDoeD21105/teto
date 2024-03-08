from .views import *


from django.urls import path


urlpatterns = [
    path("", ProductClass.as_view(), name="Home"),
    path("add_prod/", ProdAddClass.as_view(), name= "add_prod"),
    path("contact/", ContactClass.as_view(), name= "contact"),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name='post'),
    #path("login/", LoginUserr.as_view(), name="login"),
    #path("register/", RegisterUserr.as_view(), name="register"),
    #path("users/", UsersClass.as_view(), name="userrs")
]