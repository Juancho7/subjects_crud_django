from django.urls import path
from .views import home, add_course, editing_course, edit_course, delete_course

urlpatterns = [
    path("", home),
    path("add_course/", add_course),
    path("editing_course/<code>", editing_course),
    path("edit_course/", edit_course),
    path("delete_course/<code>", delete_course),
]
