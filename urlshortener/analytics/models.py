from django.db import models

# Create your models here.
from shortener.models import shortURL

class ClickEventManager(models.Manager):

	def create_event(self, instance):
		if isinstance(instance, shortURL):
			obj, created = self.get_or_create(short_url=instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):

	short_url 	= models.OneToOneField(shortURL, on_delete=models.CASCADE)
	count		= models.IntegerField(default=0)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{}".format(self.count)