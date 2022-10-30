from django.shortcuts import redirect, get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from appMain.models import Teacher, Classe, Eleve, Presence
from .forms import addStudentForm, updateStudentForm, addClasseForm, addTeacherForm
from django.utils.text import slugify
import json
from django.contrib import messages

User = get_user_model()


class RedirectToPreviousMixin:

    default_redirect = "/"

    def get(self, request, *args, **kwargs):
        request.session["previous_page"] = request.META.get(
            "HTTP_REFERER", self.default_redirect
        )
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session["previous_page"]


# Create teacher
class AddTeacher(LoginRequiredMixin, generic.TemplateView):
    form_class = addTeacherForm
    template_name = "appO/CRUD/teacher/addTeacher.html"
    page_title = "Add Teacher"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class(), "page_title": self.page_title}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        name = request.POST.get("nom")
        name1 = request.POST.get("prenom")
        username = f"{name}_{name1}"
        if form.is_valid:
            user = User.objects.create_user(
                username=username,
                email="{}@example.com".format(username),
                password=request.POST.get("dob"),
                is_visitor=False,
                is_teacher=True,
            )
            f = form.save(commit=False)
            f.t_user = user
            f.slug = slugify(request.POST.get("nom") + "-" + request.POST.get("prenom"))
            f.save()
            return redirect("appO:o_listTeacher")


# Retrive teacher
class o_listTeacher(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/CRUD/teacher/o_listTeacher.html"

    def get(self, request, *args, **kwargs):
        listTeacher = Teacher.objects.all()
        context = {"listTeacher": listTeacher, "page_title": "List Teacher"}
        return render(request, self.template_name, context)


class o_view_teacher(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/CRUD/teacher/o_teacher_details.html"

    def get(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        teacher = get_object_or_404(Teacher, slug=slug)
        return render(request, self.template_name, {"teacher": teacher})


# Update teacher
class UpTeacher(LoginRequiredMixin, RedirectToPreviousMixin, UpdateView):
    model = Teacher
    template_name = "appO/CRUD/teacher/upTeacher.html"
    form_class = addTeacherForm
    extra_context = {"page_title": "Update Teacher"}


# Delete teacher
class DelTeacher(LoginRequiredMixin, RedirectToPreviousMixin, DeleteView):
    model = Teacher
    template_name = "appO/CRUD/delObj.html"
    extra_context = {"page_title": "Delete Teacher"}


# Create classes
class AddClasses(LoginRequiredMixin, generic.TemplateView):
    form_class = addClasseForm
    template_name = "appO/CRUD/classe/addClasses.html"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class(), "page_title": "Add Classe"}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.slug = slugify(
                request.POST.get("Classe_name") + "-" + request.POST.get("school_year")
            )
            f.save()
            return redirect("appO:o_listClasses")


# Retrive teacher
class o_listClasses(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/CRUD/classe/o_listclass.html"
    extra_context = {"page_title": "Class List"}

    def get(self, request, *args, **kwargs):
        listClass = Classe.objects.all().order_by("Classe_name")
        context = {"listClass": listClass}
        return render(request, self.template_name, context)


class dashClass(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/CRUD/classe/dashboard_class.html"
    page_title = "Dashboard Classe"

    def get_context_data(self, **kwargs):
        context = super(dashClass, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["classes"] = Classe.objects.filter(pk=pk)
        context["numblistStuds"] = Eleve.objects.filter(class_id=pk).count()
        context["listStuds"] = Eleve.objects.filter(class_id=pk)
        context["page_title"] = self.page_title
        return context


# Update std
class UpClasses(LoginRequiredMixin, RedirectToPreviousMixin, UpdateView):
    model = Classe
    template_name = "appO/CRUD/classe/upClasse.html"
    form_class = addClasseForm
    extra_context = {"page_title": "Update Classe"}


# Delete classe
class DelClasses(LoginRequiredMixin, RedirectToPreviousMixin, DeleteView):
    model = Classe
    template_name = "appO/CRUD/delObj.html"
    extra_context = {"page_title": "Delete Classe"}


# Create std
class AddStudentes(LoginRequiredMixin, generic.TemplateView):
    form_class = addStudentForm
    template_name = "appO/CRUD/std/addStud.html"

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class(), "page_title": "Add Studente"}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        name = request.POST.get("nom")
        name1 = request.POST.get("prenom")
        username = f"{name}_{name1}"
        if form.is_valid:
            user = User.objects.create_user(
                username=username,
                email="{}@example.com".format(username),
                password=request.POST.get("dob"),
                is_visitor=False,
                is_student=True,
            )
            f = form.save(commit=False)
            f.user = user
            f.slug = slugify(request.POST.get("nom") + "-" + request.POST.get("prenom"))
            f.class_id = Classe.objects.filter(pk=request.POST.get("class_id")).first()
            f.save()
            return redirect("appO:o_listClasses")


# Retrive std
class o_listStudent(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/CRUD/std/o_listStud.html"
    page_title = "Student List"

    def get_context_data(self, **kwargs):
        context = super(o_listStudent, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["listStuds"] = Eleve.objects.filter(class_id=pk)
        context["classes"] = Classe.objects.filter(pk=pk)
        context["page_title"] = self.page_title
        return context


class o_view_student(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/CRUD/std/o_student_details.html"

    def get(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        student = get_object_or_404(Eleve, slug=slug)
        return render(request, self.template_name, {"student": student})


# Update std
class UpStudentes(LoginRequiredMixin, RedirectToPreviousMixin, UpdateView):
    model = Eleve
    template_name = "appO/CRUD/std/upStud.html"
    form_class = updateStudentForm
    extra_context = {"page_title": "Update Student"}


# Delete std
class DelStudentes(LoginRequiredMixin, RedirectToPreviousMixin, DeleteView):
    model = Eleve
    template_name = "appO/CRUD/delObj.html"
    extra_context = {"page_title": "Delete Student"}


class o_Att(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/o_att.html"

    def get(self, request, *args, **kwargs):
        klasname = self.kwargs["klasname"]
        listPresence = Presence.objects.all().order_by("attendance_date")
        context = {
            "listPresence": listPresence,
            "klasname": klasname,
            "page_title": "Test",
        }
        return render(request, self.template_name, context)


class o_Att_by_date(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/o_att.html"
    page_title = "Test o_Att_by_date"

    def get_context_data(self, **kwargs):
        context = super(o_Att_by_date, self).get_context_data(**kwargs)
        att_date = self.kwargs["att_date"]
        context["listPresence"] = Presence.objects.filter(attendance_date=att_date)
        context["klasname"] = self.kwargs["klasname"]
        context["page_title"] = self.page_title
        return context


class o_AttMgt(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/o_attmgt.html"
    page_title = "Student List"

    def get_context_data(self, **kwargs):
        context = super(o_AttMgt, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["listStuds"] = Eleve.objects.filter(class_id=pk)
        context["klasname"] = self.kwargs["klasname"]
        context["skooY"] = self.kwargs["skooY"]
        context["class_id"] = pk
        context["page_title"] = self.page_title
        return context


class confirm(LoginRequiredMixin, generic.TemplateView):
    def post(self, request, *args, **kwargs):
        class_id = self.kwargs["class_id"]
        listStuds = Eleve.objects.filter(class_id=class_id)
        for student in listStuds:
            status = request.POST[student.student_code]
            if status != "present":
                statu = "False"
            statu = "True"
            date_ = request.POST["mydate"]
            a = Presence(student=student, attendance_date=date_, status=statu)
            a.save()
        return HttpResponse("Ok")


# OHome views here.
class oHomeview(LoginRequiredMixin, generic.TemplateView):
    template_name = "appO/ohome.html"
    extra_context = {"page_title": "Home"}
