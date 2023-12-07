from django.shortcuts import render

# Create your views here.

def root(request):

    return render(request,"dr_page.html")

def hospital(request):
 return render(request,"hospital.html")