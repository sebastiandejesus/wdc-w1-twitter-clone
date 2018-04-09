from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    username = models.CharField(max_length=20)
    tweet = models.CharField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "<{}-Tweets>".format(self.username.title())
