from django.contrib import admin
from .models import Eleve, Classe, Teacher, Presence


admin.site.register(Eleve)
admin.site.register(Classe)
admin.site.register(Teacher)
admin.site.register(Presence)
