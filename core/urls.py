
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budget_app.urls')),
    path('', include('social_django.urls')),
    path('api/', include('budget_api.urls')),
]
