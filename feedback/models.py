from django.db import models
from django.db.models.deletion import CASCADE

class Feedback(models.Model):
    user_id = models.ForeignKey('accounts.UserAccount', on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    domain = models.CharField(max_length=100)
    rating = models.IntegerField()
    chatsession = models.JSONField()
