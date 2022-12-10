from django.shortcuts import render
from . models import *

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Message.objects.create(name=name, phone=phone, email=email, message=message)

    info_school = Welcome_header.objects.all().last()
    about = About.objects.all().last()
    info_teachers = Info_Teachers.objects.all().last()
    teachers = Teachers.objects.all()
    vehicles = Vehicles_Facility.objects.all().last()
    kind_ve = Kind_of_vehicles.objects.all()
    student = Student.objects.all().last()
    info_student = Info_Student.objects.all().last()
    contact = Contact.objects.all().last()
    footer = Footer.objects.all().last()

    return render(request, 'home/index.html', context={"info_school": info_school, 
    "about": about, "teachers": teachers,
    "info_teacher": info_teachers, "vehicles": vehicles,
    "kind_ve": kind_ve, "student": student,
    "info_student": info_student, "contact": contact,
    "footer": footer, })

