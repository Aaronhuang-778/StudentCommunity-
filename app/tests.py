import os
from random import randint

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'BuaaTalk.settings'
django.setup()

from django.test import TestCase
from app import tools
from app.models import User, Post, Like, Unlike, Comment, Keyword, Follow_star


# Create your tests here.

class test(TestCase):
    def test(self):
        # a = tools.signin("2", "12")
        # print(a)
        # print((User.objects.all())[0].user_name)
        # eval('tools.userAttributeChange(1, "follow_num", "add")')

        # tools.change(1,"follow_num","+","User")
        # user = User.objects.filter(id=1)[0]
        # print(user.follow_num)
        # tools.delPost(1)
        # tools.like(1, 1)
        # post = Post.objects.filter(id=1)[0]
        # print(post.__dict__)
        # print(Like.objects.all())
        # tools.getUser(3)
        # print(randint(1,3))
        flag, res = tools.search("213")
        print(res['post'])
        print(len(res['post']))