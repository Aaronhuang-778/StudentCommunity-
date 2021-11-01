from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, unique=True)
    user_phone = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    follow_num = models.IntegerField(default=0)
    star_num = models.IntegerField(default=0)
    post_num = models.IntegerField(default=0)
    picture = models.CharField(max_length=255, null=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    like_number = models.IntegerField(default=0)
    unlike_number = models.IntegerField(default=0)
    comment_number = models.IntegerField(default=0)
    user_id = models.IntegerField()
    keyword_id = models.IntegerField()
    post_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()


class Unlike(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.CharField(max_length=10000)
    comment_date = models.DateTimeField(auto_now_add=True)


class Keyword(models.Model):
    id = models.AutoField(primary_key=True)
    keyword_name = models.CharField(max_length=255, unique=True)


class Follow_star(models.Model):
    id = models.AutoField(primary_key=True)
    follow_id = models.IntegerField()
    star_id = models.IntegerField()
