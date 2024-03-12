from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("signup/", views.signup),
    path("register/", views.insert),
    path("login-user/", views.login_user),
    path("login/", views.login),
    path("data/", views.show_data),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>", views.update),
    path("edit/<int:id>", views.edit),
]