from django.db import models
from django.db.models.deletion import CASCADE

class Feedback(models.Model):
    user_id = models.ForeignKey('accounts.UserAccount', on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    domain = models.CharField(max_length=100)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=200)
    chatsession = models.JSONField()
    resolved = models.BooleanField(default=False, null=True)
