from .serializers import *


class CelestialBodyViewSet(viewsets.ModelViewSet):
    queryset = CelestialBody.objects.all()
    serializer_class = CelestialBodySerializer


class LaunchParamsViewSet(viewsets.ModelViewSet):
    queryset = LaunchParams.objects.all()
    serializer_class = LaunchParamsSerializer


class StartParamsViewSet(viewsets.ModelViewSet):
    queryset = CelestialBody.objects.all()
    serializer_class = StartParamsSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = CelestialBody.objects.all()
    serializer_class = ResultSerializer
