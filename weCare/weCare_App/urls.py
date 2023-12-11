
from django.urls import path, include
from . import views
urlpatterns = [
    path('specialities',views.specialities),
    path('hospitals',views.hospitals),
    path('doctors',views.doctors),
    path('',views.root),
    path('register', views.register),
    path('register/page',views.register_page),
    path('loginPage',views.loginPage),
    path('feedback', views.feedBack),
    path('feedback/function',views.feedback_function),
    path('destroy', views.logout),
    path('login', views.login),
    path('logout',views.logout),
    path('function/book',views.function_book),
    path('book',views.book),
    path('api/fetch-hospitals/<int:doctor_id>', views.fetch_hospitals, name='fetch_hospitals'),
    path('api/fetch-dates/<int:doctor_id>/<int:hospital_id>', views.fetch_dates, name='fetch_dates'),
    path('api/fetch-times/<int:date_id>', views.fetch_times, name='fetch_times'),
    path('book_an_appointment',views.book_an_appointment),
    path('appointment_booked_successfully',views.appointment_booked_successfully)

]