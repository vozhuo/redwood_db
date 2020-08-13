from django.shortcuts import render
from redwood.models import Classes
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json


def index(request):
    return render(request, 'index.html')


def data(request):
    # Redwood
    redwood = list(Classes.objects.all().values())[:5]
    redwood = [redwood[0], redwood[4]]
    print(redwood)
    return JsonResponse(redwood, safe=False)

# def image(request):
#     # redwood_id = json.loads(request.body.decode()).get('id') for POST
#     redwood_id = request.GET.get('id')
#     print(redwood_id)
#     images = list(Images.objects.filter(redwood_id=redwood_id).values())
#     print(images)
#     return JsonResponse(images, safe=False)
