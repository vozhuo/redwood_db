from django.shortcuts import render
from redwood.models import Classes, Filters
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json


def index(request):
    return render(request, 'index.html')


def data(request):
    # Redwood
    redwood = list(Classes.objects.all().values())
    print(redwood)
    return JsonResponse(redwood, safe=False)


def filters(request):
    # Redwood Filters
    redwood = list(Filters.objects.all().values())
    print(redwood)
    return JsonResponse(redwood, safe=False)
