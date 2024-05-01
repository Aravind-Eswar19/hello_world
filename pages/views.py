from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):   #template folder in project level
    template_name = 'home.html'

# def homePageView(request):    # template folder in app level
#     return render(request, 'pages/home.html')


class AboutPageView(TemplateView):
    template_name = 'about.html'
    