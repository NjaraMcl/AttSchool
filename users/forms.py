from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from users.models import Profile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text="Enter Email Address",
        widget=forms.TextInput(
            attrs={"class": "form-control myitem", "placeholder": "Your Email"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": ("form-control myitem"), "placeholder": ("Username")}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": ("form-control myitem"), "placeholder": ("Password")}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": ("form-control myitem"), "placeholder": ("Repeat password")}
        )

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": ("form-control myitem"), "placeholder": ("Username")}
        )
        self.fields["email"].widget.attrs.update(
            {"class": ("form-control myitem"), "placeholder": ("e-mail")}
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].widget.attrs.update({"class": ("form-control myitem")})
