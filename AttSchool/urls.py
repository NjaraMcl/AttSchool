from AttSchool import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appMain.urls")),
    path("", include("appV.urls")),
    path("", include("appE.urls")),
    path("", include("appT.urls")),
    path("", include("appO.urls")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("register/", user_views.UserCreateView.as_view(), name="register"),
    path("profile/", user_views.ProfileView.as_view(), name="profile"),
    path("profile/update", user_views.UpdateProfileView.as_view(), name="upprofile"),
    path("logout/", user_views.logout_user.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
