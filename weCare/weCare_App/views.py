from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.views.decorators.cache import never_cache

def specialities(request):
    return render(request,"specialities.html")

def hospitals(request):
    return render(request,"hospital.html")

def doctors(request):
    return render(request,"dr_page.html")
# Create your views here.

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
    all_specialities =  Speciality.objects.all()
    all_hosptials = Hospital.objects.all()
    all_doctors = Doctor.objects.all()
    print ("am here")
    print( all_specialities)
    context = {'all_specialities': all_specialities,'all_hosptials':all_hosptials,'all_doctors':all_doctors }
    return render (request,'bookanappointment.html', context)

def book(request):
    return redirect('/')

def logout(request):
    del request.session['id']
    return redirect("/")


@never_cache
def fetch_hospitals(request, doctor_id):
    try:
        print(doctor_id)
        doctor = Doctor.objects.get(pk=doctor_id)
        hospitals_of_selected_doctor = doctor.hospital.all()
        return JsonResponse({'hospitals': serialize('json', hospitals_of_selected_doctor)})
        # return JsonResponse({'doctor_id': doctor_id})
    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)


def book_an_appointment(request):
    return render(request,'bookanappointment.html')



def feedback_function(request):
    patient_id = request.session['id']
    patient_obj = Patient.objects.get(id = patient_id)
    feedBack = request.POST['feedback']
    date = request.POST['date']
    title = request.POST['title']
    feedback = Feedback.objects.create(
        patient = patient_obj,description = feedBack,title = title,date = date )
    patient_obj.feedback.add(feedback)

    return redirect('/feedback')
