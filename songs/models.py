from django.db import models
from datetime import timedelta

class Performer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    length = models.IntegerField()
    performer = models.ForeignKey(Performer, blank=True, default='')

    def __str__(self):
        return '%s by %s' % (self.title, self.artist)
        # return '{} by {}'.format(self.title, self.artist)
