from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

class TempView(TemplateView):
	template_name = 'temp.html'

class MainRedirectView(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		return '#'
		# return reverse_lazy('namespace:view_name', kwargs='...')