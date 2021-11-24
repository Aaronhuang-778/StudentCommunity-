import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'BuaaTalk.settings'
django.setup()
from app.models import User, Post, Like, Unlike, Comment, Keyword, Follow_star, Message


def register(user_name, user_phone, password):
    try:
        User.objects.create(user_name=user_name, user_phone=user_phone, password=password, picture='default')
        return True
    except Exception as e:
        print(str(e))
        return False


def signin(user_phone, password):
    try:
        user = User.objects.filter(user_phone=user_phone)[0]
        return password == user.password, user.dict()
    except Exception as e:
        print(str(e))
        return False, -1


def publishPost(post_title, content, user_id, keyword):
    try:
        # keyword = Keyword.objects.filter(id=keyword_id)[0]
        post = Post.objects.create(post_title=post_title, content=content, user_id=user_id,
                                   keyword_name=keyword['keyword_name'])
        addsub(user_id, 'post_num', '+', 'User')
        return True, post.dict()
    except Exception as e:
        print(str(e))
        return False, None


def delPost(post_id):
    try:
        post = Post.objects.filter(id=post_id)[0]
        addsub(post.user_id, 'post_num', '-', 'User')
        Like.objects.filter(post_id=post_id).delete()
        Unlike.objects.filter(post_id=post_id).delete()
        Comment.objects.filter(post_id=post_id).delete()
        post.delete()
        return True
    except Exception as e:
        print(str(e))
        return False


def like(post_id, user_id):
    try:
        like = Like.objects.create(post_id=post_id, user_id=user_id)
        addsub(post_id, 'like_number', '+', 'Post')
        return True, like.dict()
    except Exception as e:
        print(str(e))
        return False, None


def cancellike(like_id):
    try:
        like = Like.objects.filter(id=like_id)[0]
        addsub(like.post_id, 'like_number', '-', 'Post')
        like.delete()
        return True
    except Exception as e:
        print(str(e))
        return False


def unlike(post_id, user_id):
    try:
        unlike = Unlike.objects.create(post_id=post_id, user_id=user_id)
        addsub(post_id, 'unlike_number', '+', 'Post')
        return True, unlike.dict()
    except Exception as e:
        print(str(e))
        return False, None


def cancelunlike(unlike_id):
    try:
        unlike = Unlike.objects.filter(id=unlike_id)[0]
        addsub(unlike.post_id, 'unlike_number', '-', 'Post')
        unlike.delete()
        return True
    except Exception as e:
        print(str(e))
        return False


def comment(post_id, user_id, content):
    try:
        comment = Comment.objects.create(post_id=post_id, user_id=user_id, content=content)
        addsub(post_id, 'comment_number', '+', 'Post')
        return True, comment.dict()
    except Exception as e:
        print(str(e))
        return False, None


def cancelcomment(comment_id):
    try:
        comment = Comment.objects.filter(id=comment_id)[0]
        addsub(comment.post_id, 'comment_number', '-', 'Post')
        comment.delete()
        return True
    except Exception as e:
        print(str(e))
        return False


def follow(follow_id, star_id):
    try:
        follow_star = Follow_star.objects.create(follow_id=follow_id, star_id=star_id)
        addsub(follow_id, 'star_num', '+', 'User')
        addsub(star_id, 'follow_num', '+', 'User')
        return True, follow_star.dict()
    except Exception as e:
        print(str(e))
        return False, None


def cancelfollow(follow_star_id):
    try:
        follow_star = Follow_star.objects.filter(id=follow_star_id)[0]
        addsub(follow_star.follow_id, 'star_num', '-', 'User')
        addsub(follow_star.star_id, 'follow_num', '-', 'User')
        follow_star.delete()
        return True
    except Exception as e:
        print(str(e))
        return False


def message(send_user_id, receive_user_phone, content):
    try:
        user = User.objects.filter(user_phone=receive_user_phone)[0]
        message = Message.objects.create(send_user_id=send_user_id, receive_user_id=user.id, content=content)
        return True, message.dict()
    except Exception as e:
        print(str(e))
        return False, None


def cancelmessage(message_id):
    try:
        message = Message.objects.filter(id=message_id)[0]
        message.delete()
        return True
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


def getUser(user_id):
    try:
        user = User.objects.filter(id=user_id)[0]
        res = user.dict()
        message = Message.objects.filter(receive_user_id=user_id)
        messages = [i.dict() for i in message]
        res["message"] = messages
        return True, res
    except Exception as e:
        print(str(e))
        return False, None


def getPost(post_id, user_id):
    try:
        post = Post.objects.filter(id=post_id)[0]
        res = post.dict()
        commment = Comment.objects.filter(post_id=post_id)
        commments = [i.dict() for i in commment]
        likes = Like.objects.filter(post_id=post_id, user_id=user_id)
        if len(likes) == 0:
            res["like_id"] = -1
        else:
            res["like_id"] = likes[0].id
        unlikes = Unlike.objects.filter(post_id=post_id, user_id=user_id)
        if len(unlikes) == 0:
            res["unlike_id"] = -1
        else:
            res["unlike_id"] = unlikes[0].id
        res["commment"] = commments
        user_name = User.objects.filter(id=res['user_id'])[0].user_name
        res['user_name'] = user_name
        return True, res
    except Exception as e:
        print(str(e))
        return False, None


def getPostList():
    try:
        res = {}
        post = Post.objects.all().order_by('-post_date')
        posts = []
        for i in post:
            p = i.dict()
            user_name = User.objects.filter(id=p['user_id'])[0].user_name
            p['user_name'] = user_name
            labels = []
            if p['keyword_name'] is not None:
                labels.append(p['keyword_name'])
            posts.append(p)
        res["post"] = posts
        return True, res
    except Exception as e:
        print(str(e))
        return False, None


def getMyPostList(user_id):
    try:
        res = {}
        post = Post.objects.filter(user_id=user_id).order_by('-post_date')
        posts = [i.dict() for i in post]
        res["post"] = posts
        return True, res
    except Exception as e:
        print(str(e))
        return False, None


def getKeywordList():
    try:
        keyword = Keyword.objects.all()
        keywords = [i.dict() for i in keyword]
        return True, keywords
    except Exception as e:
        print(str(e))
        return False, None
