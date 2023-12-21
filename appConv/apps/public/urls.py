from django.urls import path
from .views import Home, About, Services, Test

app_name = "public_app"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("nosotros/", About.as_view(), name="about"),
    path("servicios/", Services.as_view(), name="services"),
    path("test/", Test.as_view(), name="test"),
]
