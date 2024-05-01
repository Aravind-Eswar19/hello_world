from django.shortcuts import render, HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')

