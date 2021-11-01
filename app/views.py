import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app import tools


def register(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.register(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def signin(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.signin(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def publishPost(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.signin(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def delPost(request):
    res = {}
    data = json.loads(request.Get.get('data'))
    flag = tools.delPost(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def like(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.like(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def cancellike(request):
    res = {}
    data = json.loads(request.Get.get('data'))
    flag = tools.cancellike(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def unlike(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.unlike(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def cancelunlike(request):
    res = {}
    data = json.loads(request.Get.get('data'))
    flag = tools.cancelunlike(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def comment(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.comment(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def cancelcomment(request):
    res = {}
    data = json.loads(request.Get.get('data'))
    flag = tools.cancelcomment(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def follow(request):
    res = {}
    data = json.loads(request.body)
    flag = tools.follow(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)


def cancelfollow(request):
    res = {}
    data = json.loads(request.Get.get('data'))
    flag = tools.cancelfollow(**data)
    if flag:
        res = {"code": 20000}
    else:
        res = {"code": 40000}
    return JsonResponse(res)
