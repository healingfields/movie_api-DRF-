from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=150)
    about = models.CharField(max_length=250)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    name = models.CharField(max_length=150)
    storyline = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
