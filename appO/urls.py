from django.urls import path
from . import views

app_name = "appO"

urlpatterns = [
    # Home views
    path("ohome/", views.oHomeview.as_view(), name="ohome"),
    # Teacher views
    path("Teacher/list/", views.o_listTeacher.as_view(), name="o_listTeacher"),
    # CRUD Teacher views
    path("Teacher/add/", views.AddTeacher.as_view(), name="AddTeacher"),
    path(
        "Teacher/<slug:slug>",
        views.o_view_teacher.as_view(),
        name="o_teacherdetail",
    ),
    path(
        "Teacher/<slug:slug>/update/",
        views.UpTeacher.as_view(),
        name="UpdateTeacher",
    ),
    path(
        "Teacher/<slug:slug>/delete/",
        views.DelTeacher.as_view(),
        name="DeleteTeacher",
    ),
    # Classe views
    path(
        "Classes/list/",
        views.o_listClasses.as_view(),
        name="o_listClasses",
    ),
    path("Classes/<int:pk>", views.dashClass.as_view(), name="dashClass"),
    # CRUD Classe views
    path("Classes/add/", views.AddClasses.as_view(), name="AddClasses"),
    path(
        "Classes/<slug:slug>/update/", views.UpClasses.as_view(), name="UpdateClasses"
    ),
    path(
        "Classes/<slug:slug>/delete/", views.DelClasses.as_view(), name="DeleteClasses"
    ),
    # Student views
    path("<int:pk>/Student/list/", views.o_listStudent.as_view(), name="o_listStudent"),
    # CRUD Student views
    path("Student/add/", views.AddStudentes.as_view(), name="AddStudentes"),
    path("Student/<slug:slug>", views.o_view_student.as_view(), name="o_studentdetail"),
    path(
        "Student/<slug:slug>/update/",
        views.UpStudentes.as_view(),
        name="UpdateStudentes",
    ),
    path(
        "Student/<slug:slug>/delete/",
        views.DelStudentes.as_view(),
        name="DeleteStudentes",
    ),
    # Attendance views
    path(
        "ohome/listClasses/<str:klasname>/o_attendence/",
        views.o_Att.as_view(),
        name="o_attendence",
    ),
    path(
        "ohome/listClasses/<str:klasname>/<str:skooY>/<int:pk>/o_attmgt/",
        views.o_AttMgt.as_view(),
        name="o_attmgt",
    ),
    path(
        "ohome/listClasses/<int:class_id>/confirm",
        views.confirm.as_view(),
        name="confirm",
    ),
]
