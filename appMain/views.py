from django.shortcuts import redirect
from django.views import generic
from django.db.models import Q


class Aboutusview(generic.TemplateView):
    template_name = "appMain/aboutus.html"
    extra_context = {"page_title": "About Us"}


class gHomeview(generic.TemplateView):
    template_name = "appMain/ghome.html"
    extra_context = {"page_title": "Home"}


class Homeview(generic.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("appMain:ghome")
        if request.user.is_visitor:
            return redirect("appV:vhome")
        if request.user.is_student:
            return redirect("appE:ehome")
        if request.user.is_teacher:
            return redirect("appT:thome")
        if request.user.is_overseer:
            return redirect("appO:ohome")
