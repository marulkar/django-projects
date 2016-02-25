from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Projects(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	technologies_used = models.CharField(max_length = 10)
	pub_date = models.DateTimeField('date published')

def __unicode__(self):
	return self.title