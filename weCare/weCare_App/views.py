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
        img = request.POST['img']
        new_Patient = Patient.objects.create(
            first_name = fName, last_name = lName, email = email, password = pw_hash,gender = gender, phone = phone, image = img )
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
def login(request):
     return render(request,'login.html')


def loginPage(request):
    errors = Patient.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/login')
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
    patient = Patient.objects.get(id = request.session['id'])
    all_specialities =  Speciality.objects.all()
    all_hosptials = Hospital.objects.all()
    all_doctors = Doctor.objects.all()
    context = {
        "user" : patient,
        'all_specialities': all_specialities,
        'all_hosptials':all_hosptials,
        'all_doctors':all_doctors,
    }
    return render(request,'bookanappointment.html',context)


def function_book(request):
    if "id" in request.session:
        
        return redirect("feedBack.html")
    else:
        return redirect('/login')

def book(request):
    if request.method == 'POST':
        speciality = request.POST['speciality']
        doctor_id = request.POST['doctor']
        doctor_object = Doctor.objects.get(id=doctor_id)
        request.session['doctor_first_name'] = doctor_object.first_name
        request.session['doctor_last_name'] = doctor_object.last_name
        hospital_id = request.POST['hospital']
        hospital_object = Hospital.objects.get(id=hospital_id)
        request.session['hospital_name'] = hospital_object.name
        date_id = request.POST['date']
        date_object = TimeSlot.objects.get(id=date_id)
        request.session['booked_date'] =  date_object.date.strftime('%Y-%m-%d')
        time_id = request.POST['time']
        time_object = TimeSlot.objects.get(id=time_id)
        request.session['booked_time'] =  time_object.time.strftime('%H:%M:%S')
        patient_id = request.session['id']
        patient_object = Patient.objects.get(id=patient_id)
        request.session['patient_first_name'] = patient_object.first_name
        request.session['patient_last_name'] =  patient_object.last_name
        #create appointment
        created_appointment = Appointment.objects.create(
            date=date_object.date,
            time=time_object.time,
            doctor=doctor_object,
            hospital=hospital_object,
            patient=patient_object
        )
        # Update the time_object is_available value to False
        time_object.is_available = False
        time_object.save()

    return redirect('/appointment_booked_successfully')

def appointment_booked_successfully(request):
    return render(request,'appointment_booked_successfully.html')


def logout(request):
    del request.session['id']
    return redirect("/")

def function_book(request):
    if "id" in request.session:
        
        return redirect('/book_an_appointment')
    else:
        return redirect('/login')

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

@never_cache
def fetch_dates(request, doctor_id, hospital_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        hospital = Hospital.objects.get(id=hospital_id)
        dates_of_selected_doctor_and_hospital = TimeSlot.objects.filter(doctor=doctor,hospital=hospital)
        print(dates_of_selected_doctor_and_hospital)
        return JsonResponse({'available_dates': serialize('json', dates_of_selected_doctor_and_hospital)})
    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'No available dates found'}, status=404)

@never_cache
def fetch_times(request, date_id):
    try:
        date = TimeSlot.objects.get(id=date_id)
        date_value = date.date
        time_slots_of_this_date = TimeSlot.objects.filter(date= date_value,  is_available=True)
        print(time_slots_of_this_date)
        return JsonResponse({'available_times': serialize('json',time_slots_of_this_date )})
    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'No available dates found'}, status=404)
  
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

