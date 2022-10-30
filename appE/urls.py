from django.urls import path
from . import views

app_name = "appE"

urlpatterns = [
    path("ehome/", views.eHomeview.as_view(), name="ehome"),
]
