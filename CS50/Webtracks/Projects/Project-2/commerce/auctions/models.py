from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField("Listing", blank=True, related_name="listing_users")

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    winner_pk = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    bid = models.IntegerField()
    img_url = models.URLField(blank=True)
    category = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}: {self.title} ${self.bid}"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} on {self.listing.title}"

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    bid = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.bid}"
