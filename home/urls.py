from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.dasbor, name='dasbor'),
    path('akun/', views.akun, name='akun'),
    path('akun/edit/', views.editAkun, name='edit_akun'),

    path('training/', views.dataTraining, name='training'),
    path('training/add', views.createTraining, name='create_training'),
    path('training/update/<str:id>', views.updateTraining, name='update_training'),
    path('training/delete/<str:id>', views.deleteTraining, name='delete_training'),

    path('training/see-training/<str:id>', views.seeDataTraining, name="see_data_training"),
    path('training/update-training/<str:id>', views.updateDataTraining, name="update_data_training"),
    path('training/add-training/<str:id>', views.createDataTraining, name="create_data_training"),
    path('training/add-attribute/', views.createAttribute, name="create_attribute"),

    path('lab/', views.lab, name='lab'),
    path('lab/add/', views.createLab, name='create_lab'),
    path('lab/update/<str:id>', views.updateLab, name='update_lab'),
    path('lab/delete/<str:id>', views.deleteLab, name='delete_lab'),

    path('pakar/knn/', views.pakarKNN, name='pakar_knn'),
]
