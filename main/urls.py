from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="roof"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("sources/", views.sources, name="sources"),
    path("contact_success", views.contact_success, name="contact_success"),
]
