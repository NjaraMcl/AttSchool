from django import forms
from appMain.models import Eleve, Classe, Teacher


class addTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "nom",
            "prenom",
            "dob",
            "pob",
            "gender",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nom"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Nom")}
        )
        self.fields["prenom"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Prénom")}
        )
        self.fields["dob"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Date of birth")}
        )
        self.fields["pob"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Place of birth")}
        )
        self.fields["gender"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Gender")}
        )


class addStudentForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = [
            "student_code",
            "nom",
            "prenom",
            "dob",
            "pob",
            "gender",
            "class_id",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student_code"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Student code")}
        )
        self.fields["nom"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Nom")}
        )
        self.fields["prenom"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Prénom")}
        )
        self.fields["dob"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Date of birth")}
        )
        self.fields["pob"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Place of birth")}
        )
        self.fields["gender"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Gender")}
        )
        self.fields["class_id"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Classe")}
        )


class updateStudentForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = [
            "student_code",
            "nom",
            "prenom",
            "dob",
            "pob",
            "gender",
            "class_id",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student_code"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Student code")}
        )
        self.fields["nom"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Nom")}
        )
        self.fields["prenom"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Prénom")}
        )
        self.fields["dob"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Date of birth")}
        )
        self.fields["pob"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Place of birth")}
        )
        self.fields["gender"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Gender")}
        )
        self.fields["class_id"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Classe")}
        )


class addClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ["Classe_name", "school_year", "teacher_responsable"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["Classe_name"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Classe Name")}
        )
        self.fields["school_year"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("School Year")}
        )
        self.fields["teacher_responsable"].widget.attrs.update(
            {"class": ("form-control"), "placeholder": ("Responsable")}
        )
