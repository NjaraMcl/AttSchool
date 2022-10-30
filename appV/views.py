from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class vHomeview(LoginRequiredMixin, generic.TemplateView):
    template_name = "appV/vhome.html"
    extra_context = {"page_title": "Home"}
