from django.contrib import admin
from .models import Eleve, Classe, Teacher, Presence


class EleveAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "prenom",
        "gender",
        "class_id",
    )


admin.site.register(Eleve, EleveAdmin)
admin.site.register(Classe)
admin.site.register(Teacher)
admin.site.register(Presence)
