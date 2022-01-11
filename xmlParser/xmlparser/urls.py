from django.urls import path
from . import views
from django.contrib import messages


app_name = 'xmlparser'

urlpatterns = [
    path('', views.filesCreateView.as_view(), name='dodaj'),

]