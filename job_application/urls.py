from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage, name='index'),
    path('about',views.about, name='about'),
    path('Homepage/',views.Homepage, name="Homepage"),
    path('index/',views.index,name='index')
]