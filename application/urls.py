
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contactus'),
    path('desc/<int:id>',views.desc,name='desc'),
    path('signup',views.sign_up,name='signup'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('enroll',views.enroll,name='enroll'),
    path('enrollmore',views.enrollmore,name='enrollmore'),
    path('final',views.final,name='final'),
    path('remove/<sub>',views.remove,name='remove'),
]
