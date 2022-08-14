from django.urls import path
from .views import main, logout, landing



urlpatterns = [
    path('', main, name='main'),
    path('logout/', logout, name='logout'),
    path('landing/', landing, name='landing'),

]
