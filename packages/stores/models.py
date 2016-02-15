from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s[%s]" % (self.name, self.id)


class EmployeeTitle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s[%s]" % (self.title, self.id)
