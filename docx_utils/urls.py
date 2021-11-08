from django.urls import path, include

from  docx_utils import views

urlpatterns = [
    path('contract/', views.contract)
]