from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class eHomeview(LoginRequiredMixin, generic.TemplateView):
    template_name = "appE/ehome.html"
    extra_context = {"page_title": "Home"}
