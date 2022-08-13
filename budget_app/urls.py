from django.urls import path
from .views import main, logout

urlpatterns = [
    path('', main, name='main'),
    path('logout/', logout, name='logout'),

]