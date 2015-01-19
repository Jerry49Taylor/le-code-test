from django.contrib.auth.models import User
from django.db import models


class ItemAbstract(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PhotoItem(ItemAbstract):
    image = models.ImageField()


class TweetItem(ItemAbstract):
    text = models.CharField(max_length=150)
