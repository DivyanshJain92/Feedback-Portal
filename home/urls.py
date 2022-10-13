from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("feedback",views.feedback,name='feedback'),
    path("index",views.index,name='home'),
    path("view",views.view,name='view'),
    path("user_login",views.user_login,name='user_login'),
    path("how",views.how,name='how'),
    path("about",views.about,name='about'),
    path("logout",views.logout,name='logout')
    # path("feedback",views.feedback,name='feedback'),
    # path("about",views.about,name='about'),
    # path("service",views.service,name='service'),
    # path("contact",views.contact,name='contact')
]