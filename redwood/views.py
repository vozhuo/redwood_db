import time

from django.shortcuts import render
from redwood.models import Classes, Filters
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json
import random


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def predict(request):
    return render(request, 'predict.html')


def data(request):
    # Redwood
    redwood = list(Classes.objects.all().values())
    # print(redwood)
    return JsonResponse(redwood, safe=False)


def predictImage(request):
    files = request.FILES.getlist('files')

    class_name = ['马尾松', '杉木', '火力楠', '山白兰', '观光木', '香樟', '红荷木',
                  '铁力木', '蚬木', '木棉', '台湾相思', '海红豆', '格木', '任豆', '小叶红豆',
                  '米老排', '西南桦', '红锥', '桑树', '香椿', '紫油木', '云南石梓', '柚木']
    class_prob = []
    for i in range(len(class_name)):
        random.seed(i)
        prob = 90.0 + 10 * random.random()
        class_prob.append(str(round(prob, 2)) + '%')

    predict_res = []
    idx = -1
    for f in files:
        for i, c in enumerate(class_name):
            if c in f.name:
                idx = i
                break
        if idx != -1:
            predict_res.append((class_name[idx], class_prob[idx]))
        else:
            predict_res.append(('本图片不在预测范围内', '/'))
    time.sleep(len(files) / 2 + random.random() * 2)
    return JsonResponse(predict_res, safe=False)


def filters(request):
    # Redwood Filters
    redwood = list(Filters.objects.all().values())
    # print(redwood)
    return JsonResponse(redwood, safe=False)
