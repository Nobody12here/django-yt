from django.urls import path
from base.views import home, rooms, createRoom, updateRoom, deleteRoom

urlpatterns = [
    path("", home, name="home"),
    path("rooms/<str:pk>/", rooms, name="rooms"),
    path("create-room", createRoom, name="create-room"),
    path("update-room/<str:pk>/", updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", deleteRoom, name="delete-room"),
]
