from django.urls import path

from . import views

urlpatterns = [
    path('Upload_Image/',views.uploadImage),

]
