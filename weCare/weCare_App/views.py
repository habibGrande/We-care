from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
import bcrypt


def root(request):
    return render(request, 'landingpage.html')


def register_page(request):
    return render(request,'register.html')

def register(request):
    errors = Patient.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/register/page')
    else:
        fName = request.POST['first_name']
        lName = request.POST['last_name']
        email =  request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        phone = request.POST['phone_number']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        conPassword = request.POST['confrim_password']
        date = request.POST['bDate']
        new_Patient = Patient.objects.create(first_name = fName, last_name = lName, email = email, password = pw_hash,gender = gender, phone = phone )
        request.session['id']  = new_Patient.id
        return redirect('/')

def feedBack(request):
    if "id" in request.session:
        patient = Patient.objects.get(id = request.session['id'])
        context = {
            "user" : patient
        }
        return render(request, "feedBack.html", context)
    return redirect('/')
def loginPage(request):
     return render(request,'login.html')

def login(request):
    errors = Patient.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/loginPage')
    email = request.POST["email"]
    password = request.POST['password']
    patient = Patient.objects.filter(email=email)
    if patient:
        logged_user = patient[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/')
    else:
        messages.error(request,"Patient is not Exist")
    return redirect('/')

def book_an_appointment(request):
    return render (request,'bookanappointment.html')

def logout(request):
    del request.session['id']
    return redirect("/")

