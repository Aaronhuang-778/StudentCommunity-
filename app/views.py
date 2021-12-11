import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app import tools


def register(request):
    data = json.loads(request.body)
    data = data['UpData']
    flag = tools.register(**data)
    return myResponse(flag)


def checkLogin(request):
    is_login = request.session.get("is_login")
    if is_login == "1":
        flag = True
        res = request.session.get("user")
    else:
        flag = False
        res = -1
    return myResponse(flag, res)


def loginout(request):
    request.session.flush()
    return myResponse(True)


def signin(request):
    data = json.loads(request.body)
    data = data['InData']
    flag, res = tools.signin(**data)
    if flag:
        request.session["is_login"] = "1"
        request.session["user"] = res
        request.session.set_expiry(600)  # 10mins
    return myResponse(flag, res)


def publishPost(request):
    data = json.loads(request.body)
    flag, res = tools.publishPost(**data)
    return myResponse(flag, res)


def delPost(request):
    data = json.loads(request.GET.get('data'))
    flag = tools.delPost(**data)
    return myResponse(flag)


def like(request):
    data = json.loads(request.body)
    flag, res = tools.like(**data)
    return myResponse(flag, res)


def cancellike(request):
    data = json.loads(request.body)
    flag = tools.cancellike(**data)
    return myResponse(flag)


def unlike(request):
    data = json.loads(request.body)
    flag, res = tools.unlike(**data)
    return myResponse(flag, res)


def cancelunlike(request):
    data = json.loads(request.body)
    flag = tools.cancelunlike(**data)
    return myResponse(flag)


def comment(request):
    data = json.loads(request.body)
    flag, res = tools.comment(**data)
    return myResponse(flag, res)


def cancelcomment(request):
    data = json.loads(request.GET.get('data'))
    flag = tools.cancelcomment(**data)
    return myResponse(flag)


def follow(request):
    data = json.loads(request.body)
    flag, res = tools.follow(**data)
    return myResponse(flag, res)


def cancelfollow(request):
    data = json.loads(request.body)
    flag = tools.cancelfollow(**data)
    return myResponse(flag)


def message(request):
    data = json.loads(request.body)
    flag, res = tools.message(**data)
    return myResponse(flag, res)


def cancelmessage(request):
    data = json.loads(request.GET.get('data'))
    flag = tools.cancelmessage(**data)
    return myResponse(flag)


def getUser(request):
    data = json.loads(request.body)
    flag, res = tools.getUser(**data)
    return myResponse(flag, res)


def getPost(request):
    data = json.loads(request.body)
    flag, res = tools.getPost(**data)
    return myResponse(flag, res)


def search(request):
    data = json.loads(request.body)
    flag, res = tools.search(**data)
    return myResponse(flag, res)


def getPostList(request):
    flag, res = tools.getPostList()
    return myResponse(flag, res)


def getMyPostList(request):
    data = json.loads(request.GET.get('data'))
    flag, res = tools.getMyPostList(**data)
    return myResponse(flag, res)


def getKeywordList(request):
    flag, res = tools.getKeywordList()
    return myResponse(flag, res)


def myResponse(flag, data=None):
    if flag:
        res = {"code": 20000, "data": data}
    else:
        res = {"code": 40000, "data": data}
    response = JsonResponse(res)
    return response
