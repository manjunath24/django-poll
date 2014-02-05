from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=100)
    poll_image = models.FileField(upload_to='images', blank=True)
    created_by = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    ip_address = models.CharField(max_length=100)
    fingerprint = models.CharField(max_length=100)

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
