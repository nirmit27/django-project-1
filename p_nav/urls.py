from django.urls import path
from . import views

urlpatterns = [
    path('pnav/', views.pnav_view, name='pnav'),
    path('text/', views.text_view, name='text'),
]
