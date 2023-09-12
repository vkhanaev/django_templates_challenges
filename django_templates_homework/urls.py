from django.urls import path

from django_templates_homework.views.a_phone_number import get_phone_number_view
from django_templates_homework.views.b_contacts_info import contacts_info_view
from django_templates_homework.views.c_registration import registration_view
from django_templates_homework.views.d_about_us import about_us_view
from django_templates_homework.views.e_admin_page import admin_page_view
from django_templates_homework.views.f_students import students_view


urlpatterns = [
    path('phone-number/', get_phone_number_view),
    path('contacts/', contacts_info_view),
    path('registration/', registration_view),
    path('about/', about_us_view),
    path('admin/', admin_page_view),
    path('students/', students_view),
]
