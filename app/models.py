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

    def dict(self):
        map = {
            "user_id": self.id, "user_name": self.user_name, "user_phone": self.user_phone, "password": self.password,
            "follow_num": self.follow_num, "star_num": self.star_num, "post_num": self.post_num, "picture": self.picture
        }
        return map


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    like_number = models.IntegerField(default=0)
    unlike_number = models.IntegerField(default=0)
    comment_number = models.IntegerField(default=0)
    user_id = models.IntegerField()
    keyword_name = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)

    def dict(self):
        map = {
            "post_id": self.id, "post_title": self.post_title, "content": self.content, "like_number": self.like_number,
            "unlike_number": self.unlike_number, "comment_number": self.comment_number, "user_id": self.user_id,
            "keyword_name": self.keyword_name, "post_date": self.post_date
        }
        return map


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()

    def dict(self):
        map = {
            "like_id": self.id, "post_id": self.post_id, "user_id": self.user_id
        }
        return map


class Unlike(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()

    def dict(self):
        map = {
            "unlike_id": self.id, "post_id": self.post_id, "user_id": self.user_id
        }
        return map


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.CharField(max_length=10000)
    comment_date = models.DateTimeField(auto_now_add=True)

    def dict(self):
        map = {
            "comment_id": self.id, "post_id": self.post_id, "user_id": self.user_id, "content": self.content,
            "comment_date": self.comment_date
        }
        return map


class Keyword(models.Model):
    id = models.AutoField(primary_key=True)
    keyword_name = models.CharField(max_length=255, unique=True)


class Follow_star(models.Model):
    id = models.AutoField(primary_key=True)
    follow_id = models.IntegerField()
    star_id = models.IntegerField()

    def dict(self):
        map = {
            "follow_star_id": self.id, "follow_id": self.follow_id, "star_id": self.star_id
        }
        return map


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=10000)
    send_user_id = models.IntegerField()
    receive_user_id = models.IntegerField()
    message_date = models.DateTimeField(auto_now_add=True)

    def dict(self):
        map = {
            "message_id": self.id, "content": self.content, "send_user_id": self.send_user_id,
            "receive_user_id": self.receive_user_id, "message_date": self.message_date
        }
        return map
