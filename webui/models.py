"""Houses All of the config used to talk to MySQL."""
from django.db import models


class UserMaintenance(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateTimeField()

class Feedback(models.Model):
    comment = models.TextField()
