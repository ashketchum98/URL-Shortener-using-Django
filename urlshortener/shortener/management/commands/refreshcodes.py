from django.core.management.base import BaseCommand, CommandError

from shortener.models import shortURL

class Command(BaseCommand):
	help = "Refreshes all shortURL shortcodes."

	def handle(self, *args, **kwargs):
		return shortURL.objects.refresh_shortcodes()