from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_blogs, name="blog"),
    path("<int:pk>/", views.post, name="each_post"),
]
