
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Budget API",
        default_version='1.0.0',
        description="API documentation of budget_app",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budget_app.urls')),
    path('', include('social_django.urls')),
    path('api/', include('budget_api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")
    
]
