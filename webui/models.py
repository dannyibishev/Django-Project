"""Houses All of the config used to talk to MySQL."""
from django.db import models
from django.utils import timezone


class UserMaintenance(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateTimeField()

class Feedback(models.Model):
    comment = models.TextField()
    pub_date = models.DateTimeField(
        'Date Published',
        auto_now=True,
        auto_now_add=False,
    )

    def __str__(self):
        return "{com} {pub}".format(
            com=self.comment,
            pub=self.pub_date
        )





