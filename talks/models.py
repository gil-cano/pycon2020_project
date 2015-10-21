from django.db import models


class Track(models.Model):

    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Talk(models.Model):
    """docstring for Talk"""
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    track = models.ForeignKey(Track, default=1)

    def __str__(self):
        return self.title
