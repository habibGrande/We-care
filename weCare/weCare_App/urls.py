from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.root),
    path('register', views.register),
    path('register/page',views.register_page),
    path('loginPage',views.loginPage),
    path('feedback', views.feedBack),
    path('destroy', views.logout),
    path('login', views.login),
    path('bookanappointment',views.book_an_appointment),
    path('book',views.book),
    path('api/fetch-hospitals/<int:doctor_id>', views.fetch_hospitals, name='fetch_hospitals'),

]