from django.urls import path
from . import views

app_name = "appV"

urlpatterns = [
    path("vhome/", views.vHomeview.as_view(), name="vhome"),
]
