from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
