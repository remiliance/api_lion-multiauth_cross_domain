
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'lion', views.Lion, basename="lion")

swagger_routes = router.urls

urlpatterns = swagger_routes