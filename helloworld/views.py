from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view for ABOUT HomePageView
class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

# Create your views here.
