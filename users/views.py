from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile

User = get_user_model()


class logout_user(generic.View):
    template_name = "registration/loggedout.html"
    page_title = "Logout"

    def get(self, request):
        logout(request)
        return render(
            request,
            self.template_name,
            context={"page_title": self.page_title},
        )


class UserCreateView(generic.View):
    template_name = "registration/register.html"
    form_class = NewUserForm
    page_title = "Sign Up"

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            context={"form": form, "page_title": self.page_title},
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            messages.error(request, form.error_messages)
            return render(
                request,
                self.template_name,
                context={"form": self.form_class(), "page_title": self.page_title},
            )
        form.save()
        messages.success(
            request, f"Your account has been created! You are now able to log in"
        )
        return redirect("login")


class ProfileView(LoginRequiredMixin, generic.View):
    template_name = "registration/profile.html"
    page_title = "Profile"

    def get(self, request):
        return render(
            request, self.template_name, context={"page_title": self.page_title}
        )


class UpdateProfileView(LoginRequiredMixin, generic.View):
    template_name = "registration/up_profil.html"
    form_u = UserUpdateForm
    form_p = ProfileUpdateForm
    page_title = "Update Profile"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "page_title": self.page_title,
                "u_form": self.form_u,
                "p_form": self.form_p,
            },
        )

    def post(self, request):
        u_form = self.form_u(request.POST, instance=request.user)
        p_form = self.form_p(request.POST, request.FILES, instance=request.user.profile)
        if not u_form.is_valid() and not p_form.is_valid():
            msg = [u_form.errors, p_form.errors]
            messages.error(request, msg)
            context = {"u_form": self.form_u, "p_form": self.form_p}
            return render(request, self.template_name, context)
        usernm = u_form.cleaned_data.get("username")
        u_form.save()
        p_form.save()
        messages.success(request, f"The user “{usernm}” was changed successfully.")
        return redirect("profile")
