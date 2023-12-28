from django.urls import path
from .views import LoginMyApp

app_name = "myApp_app"

urlpatterns = [
    path("myApp", LoginMyApp.as_view(), name="myApp"),
]
