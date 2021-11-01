from django.urls import path, re_path
# 导入 app 应用的 views 文件
from . import views

urlpatterns = [
    re_path(r'register', views.register),  # 注册
    re_path(r'signin', views.signin),  # 登录
    re_path(r'publishPost', views.publishPost),  # 发表帖子
    re_path(r'delPost', views.delPost),  # 删除帖子
    re_path(r'like', views.like),  # 点赞
    re_path(r'cancellike', views.cancellike),  # 取消点赞
    re_path(r'unlike', views.unlike),  # 踩
    re_path(r'cancelunlike', views.cancelunlike),  # 取消踩
    re_path(r'comment', views.comment),  # 评论
    re_path(r'cancelcomment', views.cancelcomment),  # 取消评论
    re_path(r'follow', views.follow),  # 关注
    re_path(r'cancelfollow', views.cancelfollow),  # 取消关注
]
