import json

from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    return HttpResponse("OK")


def start_sim(request):
    if request.method == "POST":
        pass
    elif request.method == "PATCH":
        pass
    elif request.method == "DELETE":
        pass
    else:
        return HttpResponseBadRequest()
    pass


def get_celestial_body(request, object_id):
    """
    Renvoie un objet célèste au format JSON
    :param object_id:
    :param request:
    :return:
    """

    celestial_body = get_object_or_404(CelestialBody, pk=object_id)
    data = {
        "id": celestial_body.id,
        "name": celestial_body.name,
        "mass": celestial_body.mass,
        "radius": celestial_body.radius
    }
    return JsonResponse(json.dumps(data), safe=False)
