from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    platform = models.ForeignKey(StreamPlatform, related_name='watchlists', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Review(models.Model):

    body = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rating) + ' | ' + self.watchlist.name

