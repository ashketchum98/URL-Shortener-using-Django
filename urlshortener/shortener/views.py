from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect, Http404

from .models import shortURL
from .forms import SubmitUrlForms

from analytics.models import ClickEvent
# Create your views here.


# def shortURL_redirect_view(request, shortcode=None, *args, **kwargs):
# 	obj = get_object_or_404(shortURL, shortcode=shortcode)
# 	return HttpResponseRedirect(obj.url)

class HomeView(View):

	def get(self, request, *args, **kwargs):
		form  = SubmitUrlForms()
		context = {
			"title": "URL Shortener",
			"form": form
		}
		return render(request, "shortener/home.html",context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForms(request.POST)
		context = {
			"title": "URL Shortener",
			"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():
			url = form.cleaned_data.get("url")
			obj, created = shortURL.objects.get_or_create(url=url)
			context = {
				"obj": obj,
				"created": created
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/exists.html"
		
		return render(request, template, context)


class shortURLRedirectView(View):

	def get(self, request, shortcode=None, *args, **kwargs):
		#obj = get_object_or_404(shortURL, shortcode=shortcode)
		print(shortcode)
		qs = shortURL.objects.filter(shortcode__iexact = shortcode)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
		






