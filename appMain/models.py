from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()
sex_choice = (("Male", "Male"), ("Female", "Female"))


class Teacher(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    prenom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=sex_choice)
    dob = models.DateField(default="1980-01-01", blank=True, null=True)
    pob = models.CharField(max_length=250, blank=True, null=True)
    t_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom + " " + self.prenom

    def get_absolute_url(self):
        return reverse("appO:o_teacherdetail", kwargs={"slug": self.slug})


class Classe(models.Model):
    Classe_name = models.CharField(max_length=250, blank=True, null=True)
    school_year = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    teacher_responsable = models.ForeignKey(
        Teacher, blank=True, null=True, on_delete=models.SET_NULL
    )

    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.Classe_name
            + "("
            + self.school_year
            + ")"
            + " "
            + "Prof:"
            + " "
            + str(self.teacher_responsable)
        )


class Eleve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=250, blank=True, null=True)
    nom = models.CharField(max_length=250, blank=True, null=True)
    prenom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    dob = models.DateField(default="1980-01-01", blank=True, null=True)
    pob = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=sex_choice, blank=True, null=True)
    class_id = models.ForeignKey(
        Classe, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom + " " + self.prenom

    def get_absolute_url(self):
        return reverse("appO:o_studentdetail", kwargs={"slug": self.slug})


"""
Attendance: student, attendance_date, status
"""


class Presence(models.Model):
    student = models.ForeignKey(Eleve, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField(default="2018-10-23")
    status = models.BooleanField(default="True")
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.nom + " " + self.student.prenom
