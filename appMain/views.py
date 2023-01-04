from django.shortcuts import redirect, render
from django.views import generic
from django.db.models import Q
from appMain.models import Teacher, Classe, Eleve
import django


class Searchresultsview(generic.TemplateView):
    search_models = []  # Add your models here, in any way you find best.
    search_results = []
    for model in search_models:
        fields = [
            x for x in model._meta.fields if isinstance(x, django.db.models.CharField)
        ]
        search_queries = [Q(**{x.name + "__contains": search_query}) for x in fields]
        q_object = Q()
        for query in search_queries:
            q_object = q_object | query

        results = model.objects.filter(q_object)
        search_results.append(results)

    def get(self, request, *args, **kwargs):
        query = request.GET.get("search")
        if query == "":
            query = "None"
        results = Eleve.objects.filter(
            Q(first_name__icontains=query)
            | Q(nom__icontains=query)
            | Q(prenom__icontains=query)
        )
        context = {"query": query, "results": results, "page_title": "Search Results"}
        return render(request, self.template_name, context)


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
