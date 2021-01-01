from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('home/', views.dasbor),
    path('akun/', views.akun),
    path('akun/edit/', views.edit)
]
