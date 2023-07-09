from django.urls import include
import api.urls
from django.contrib import admin
from django.urls import path,  re_path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

api_patterns = [
    path(
        r"api/", include((api.urls.swagger_routes , ""))
    ),
]
schema_view = get_schema_view(
    openapi.Info(
        title="API Project ",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    patterns=api_patterns,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


