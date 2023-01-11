from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class SingleView(TemplateView):
    template_name = "single.html"


