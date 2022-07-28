from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *



# Create your views here.

def index(request):
    return render(request,"index.html")

def arthele(request,roll=None):
    if roll:
        try:
            context = {
                'i' : Studentfive.objects.get(roll_number=roll)
            }
            return render(request, "arts-eleventh.html",context)
        except Exception as e:
            return render(request, "arts-eleventh.html")
    return render(request, "arts-eleventh.html")


def arthtwe(request, roll=None):
    if roll:
        try:
            context = {
                'i' : Studentfour.objects.get(roll_number=roll)
            }
            return render(request,"arth-twelth.html",context)
        except Exception as e:
            return render(request,"arth-twelth.html")
    return render(request,"arth-twelth.html")
    

def commerceele(request,roll=None):
    if roll:
        try:
            context = {
                'i' : Studentthree.objects.get(roll_number=roll)
            }
            return render(request,"commerce-eleventh.html",context)
        except Exception as e:
            return render(request,"commerce-eleventh.html")
    return render(request,"commerce-eleventh.html")


def commercetwe(request,roll=None):
    if roll:
        try:
            context = {
                'i' : Studenttwo.objects.get(roll_number=roll)
            }
            return render(request,"commerce-twelth.html",context)
        except Exception as e:
            return render(request,"commerce-twelth.html")
    return render(request,"commerce-twelth.html")

def sciencetwe(request,roll=None):
    if roll:
        try:
            context = {
            'i' : Student.objects.get(roll_number=roll)
            
            }
            return render(request,"science-twelth.html",context)
        except Exception as e:
            return render(request,"science-twelth.html")
    return render(request,"science-twelth.html")


def scienceele(request,roll=None):
    if roll:
        try:
            context = {
                'i' : Studentone.objects.get(roll_number=roll)
            }
            return render(request,"science-eleventh.html",context)
        except Exception as e:
            return render(request,"science-eleventh.html")
    return render(request,"science-eleventh.html")



# ££££££££££££££££££££££££££££££££££££££££££££££££££££££££££ #

def artele(request):
    context = {
        "arthele_data" : Studentfive.objects.all()
    }
    return render(request,'students_name/artele.html',context)

def arttwe(request):
    context = {
        'arthtwe_data' : Studentfour.objects.all()
    }
    return render(request, 'students_name/arttwe.html',context)

def commele(request):
    context = {
        'commele_data' : Studentthree.objects.all()
    }
    return render(request,'students_name/commele.html',context)

def commtwe(request):
    context = {
        'commtwe_data' : Studenttwo.objects.all()
    }
    return render(request,'students_name/commtwe.html',context)

def scitwe(request):
    context = {
        'scietwe_data' : Student.objects.all()
    }
    return render(request,'students_name/scitwe.html',context)

def sciele(request):
    context = {
        'scieele_data' : Studentone.objects.all()
    }
    return render(request,'students_name/sciele.html',context)

