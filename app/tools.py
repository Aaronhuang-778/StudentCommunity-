import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'BuaaTalk.settings'
django.setup()
from app.models import User, Post, Like, Unlike, Comment, Keyword, Follow_star


def register(user_name, user_phone, password, picture):
    try:
        User.objects.create(user_name=user_name, user_phone=user_phone, password=password, picture=picture)
        return True
    except Exception as e:
        print(str(e))
        return False


def signin(user_phone, password):
    try:
        user = User.objects.filter(user_phone=user_phone)[0]
        return password == user.password
    except Exception as e:
        print(str(e))
        return False


def publishPost(post_title, content, user_id, keyword_id):
    try:
        Post.objects.create(post_title=post_title, content=content, user_id=user_id, keyword_id=keyword_id)
        addsub(user_id, 'post_num', '+', 'User')
        return True
    except Exception as e:
        print(str(e))
        return False


def delPost(post_id):
    try:
        post = Post.objects.filter(id=post_id)[0]
        addsub(post.user_id, 'post_num', '-', 'User')
        Like.objects.filter(post_id=post_id).delete()
        Unlike.objects.filter(post_id=post_id).delete()
        Comment.objects.filter(post_id=post_id).delete()
        post.delete()
    except Exception as e:
        print(str(e))
        return False


def like(post_id, user_id):
    try:
        Like.objects.create(post_id=post_id, user_id=user_id)
        addsub(post_id, 'like_number', '+', 'Post')
    except Exception as e:
        print(str(e))
        return False


def cancellike(like_id):
    try:
        like = Like.objects.filter(id=like_id)[0]
        addsub(like.post_id, 'like_number', '-', 'Post')
        like.delete()
    except Exception as e:
        print(str(e))
        return False


def unlike(post_id, user_id):
    try:
        Unlike.objects.create(post_id=post_id, user_id=user_id)
        addsub(post_id, 'unlike_number', '+', 'Post')
    except Exception as e:
        print(str(e))
        return False


def cancelunlike(unlike_id):
    try:
        unlike = Unlike.objects.filter(id=unlike_id)[0]
        addsub(unlike.post_id, 'unlike_number', '-', 'Post')
        unlike.delete()
    except Exception as e:
        print(str(e))
        return False


def comment(post_id, user_id, content):
    try:
        Comment.objects.create(post_id=post_id, user_id=user_id, content=content)
        addsub(post_id, 'comment_number', '+', 'Post')
    except Exception as e:
        print(str(e))
        return False


def cancelcomment(comment_id):
    try:
        comment = Comment.objects.filter(id=comment_id)[0]
        addsub(comment.post_id, 'comment_number', '-', 'Post')
        comment.delete()
    except Exception as e:
        print(str(e))
        return False


def follow(follow_id, star_id):
    try:
        Follow_star.objects.create(follow_id=follow_id, star_id=star_id)
        addsub(follow_id, 'star_num', '+', 'User')
        addsub(star_id, 'follow_num', '+', 'User')
    except Exception as e:
        print(str(e))
        return False


def cancelfollow(follow_star_id):
    try:
        follow_star = Follow_star.objects.filter(id=follow_star_id)[0]
        addsub(follow_star.follow_id, 'star_num', '-', 'User')
        addsub(follow_star.star_id, 'follow_num', '-', 'User')
        follow_star.delete()
    except Exception as e:
        print(str(e))
        return False


# def userAttributeChange(user_id, attribute, type):
#     try:
#         user = User.objects.filter(id=user_id)[0]
#         if type == 'add':
#             user.add(attribute)
#         elif type == 'sub':
#             user.sub(attribute)
#         user.save()
#         return True
#     except:
#         return False
def addsub(id: int, attribute: str, type: str, table=None):  # 表.字段+-=1
    temp = eval(table + '.objects.filter(id=' + str(id) + ')[0]')
    exec('temp.' + attribute + type + '=1')
    temp.save()
