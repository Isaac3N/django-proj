from django.urls import path
from .views import *

urlpatterns = [
    path("login/", loginPage, name="login"),
    path("register/", registerPage, name="register"),
    path("logout/", logoutUser, name="logout"),
    path("", home, name="home"),
    path("room/<str:pk>/", room, name="room"),
    path("profile/<str:pk>", userProfile, name="user-profile"),
    path("create-room/", createRoom, name="create-room"),
    path("update-room/<str:pk>/", updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>/", deleteMessage, name="delete-message"),


]
