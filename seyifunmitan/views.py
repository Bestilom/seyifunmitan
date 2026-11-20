from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world")


class WassupGuys(View):
    def get(self, request):
        return HttpResponse("Wassup Guys")  