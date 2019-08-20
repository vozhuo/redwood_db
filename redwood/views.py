from django.shortcuts import render
from redwood.models import Redwood, Images
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json

def index(request):
    return render(request, 'index.html')


def data(request):
    # Redwood
    redwood = list(Redwood.objects.all().values())
    print(redwood)
    return JsonResponse(redwood, safe=False)


def image(request):
    redwood_id = json.loads(request.body.decode()).get('id')
    images = list(Images.objects.filter(redwood_id=redwood_id).values())
    print(images)
    return JsonResponse(images, safe=False)
