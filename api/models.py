from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()


class CommentModel(models.Model):
    uName = models.CharField(max_length=300, blank=True, default='')
    uComment = models.CharField(max_length=2000, blank=True, default='')
    uUrl = models.CharField(max_length=300, blank=True, default='')
    uImg = models.CharField(max_length=300, blank=True, default='')
    uTime = models.CharField(max_length=300, blank=True, default='')
    endorse = models.IntegerField(default=0)
    oppose = models.IntegerField(default=0)
    hasReply = models.BooleanField(default=False)
    rName = models.CharField(max_length=300, blank=True, default='')
    rComment = models.CharField(max_length=300, blank=True, default='')
