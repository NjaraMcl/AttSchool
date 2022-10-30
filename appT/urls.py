from django.urls import path
from . import views

app_name = "appT"

urlpatterns = [
    path("thome/", views.tHomeview.as_view(), name="thome"),
]
