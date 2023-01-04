from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.Homeview.as_view(), name="home"),
    path("ghome/", views.gHomeview.as_view(), name="ghome"),
    path("aboutus/", views.Aboutusview.as_view(), name="aboutus"),
]
