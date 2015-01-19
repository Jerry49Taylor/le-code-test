from django.contrib.auth.models import User
from django.db import models
from items.models import PhotoItem, TweetItem


class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    photo_item = models.ForeignKey(PhotoItem, null=True, blank=True)
    tweet_item = models.ForeignKey(TweetItem, null=True, blank=True)
    