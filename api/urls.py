from django.urls import path, include

from .viewset import *

router = routers.DefaultRouter()
router.register(r'celestialbody', CelestialBodyViewSet)
router.register(r'launchparams', LaunchParamsViewSet)
router.register(r'startparams', StartParamsViewSet)
router.register(r'result', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
