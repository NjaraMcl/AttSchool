from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class tHomeview(LoginRequiredMixin, generic.TemplateView):
    template_name = "appT/thome.html"
    extra_context = {"page_title": "Home"}
