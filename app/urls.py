from django.urls import path, re_path
# 导入 app 应用的 views 文件
from . import views

urlpatterns = [
    re_path(r'^checkLogin', views.checkLogin),
    re_path(r'^loginout', views.loginout),
    re_path(r'^register', views.register),  # . 注册
    re_path(r'^signin', views.signin),  # . 登录
    re_path(r'^publishPost', views.publishPost),  # . 发表帖子
    re_path(r'^delPost', views.delPost),  # . 删除帖子
    re_path(r'^like', views.like),  # . 点赞
    re_path(r'^cancellike', views.cancellike),  # . 取消点赞
    re_path(r'^unlike', views.unlike),  # . 踩
    re_path(r'^cancelunlike', views.cancelunlike),  # . 取消踩
    re_path(r'^comment', views.comment),  # . 评论
    re_path(r'^cancelcomment', views.cancelcomment),  # . 取消评论
    re_path(r'^follow', views.follow),  # . 关注
    re_path(r'^cancelfollow', views.cancelfollow),  # . 取消关注
    re_path(r'^message', views.message),  # . 留言
    re_path(r'^cancelmessage', views.cancelmessage),  # . 删除留言
    re_path(r'^getUser', views.getUser),  # . 根据user_id得到user详情
    re_path(r'^getPostList', views.getPostList),  # . 得到所有post
    re_path(r'^getPost', views.getPost),  # . 根据post_id得到post，结合user_id得到是否点赞和踩,-1表示没有
    re_path(r'^getMyPostList', views.getMyPostList),  # . 得到user_id得到其post
    re_path(r'^getKeywordList', views.getKeywordList),  # . 得到keyword列表
    re_path(r'^search', views.search),  # 搜索
]
