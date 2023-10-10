from django.shortcuts import render, redirect
from .models import Course


# Create your views here.
def home(request):
    courses = Course.objects.all()
    return render(request, "manage_subjects.html", {"courses": courses})


def add_course(request):
    code = request.POST["txt_code"]
    name = request.POST["txt_name"]
    credits = request.POST["txt_credits"]

    Course.objects.create(code=code, name=name, credits=credits)
    return redirect("/")


def editing_course(request, code):
    course = Course.objects.get(code=code)

    return render(request, "edit_subject.html", {"course": course})


def edit_course(request):
    code = request.POST["txt_code"]
    name = request.POST["txt_name"]
    credits = request.POST["txt_credits"]

    course = Course.objects.get(code=code)
    course.name = name
    course.credits = credits
    course.save()

    return redirect("/")


def delete_course(request, code):
    course = Course.objects.get(code=code)
    course.delete()

    return redirect("/")
