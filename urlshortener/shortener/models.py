from django.db import models
from .utils import create_shortcode, code_generator
from .validators import validate_url
# Create your models here.

from django.conf import settings

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class shortURLManager(models.Manager):

	def all(self, *args, **kwargs):
		qs_main = super(shortURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self):
		qs = shortURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			new_codes += 1
		return "New Codes Made: {}".format(new_codes)

class shortURL(models.Model):
	url 		= models.CharField(max_length=220, validators=[validate_url])
	shortcode 	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	active		= models.BooleanField(default=True)

	objects = shortURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(shortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def get_short_url(self):
		return "http://localhost:8000/{}".format(self.shortcode)