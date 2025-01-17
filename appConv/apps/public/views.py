from django.views.generic import TemplateView
from .models import Logo



# Create your views here.
class Home(TemplateView):
    template_name = "public/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        logo = Logo.objects.filter(name="logo")
        context["logo"] = logo
        return context


# Create your views here.
class About(TemplateView):
    template_name = "public/about.html"


# Create your views here.
class Services(TemplateView):
    template_name = "public/services.html"

class Test(TemplateView):
    template_name = "errors/404.html"


