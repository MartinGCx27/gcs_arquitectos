from django.views.generic import View
from django.shortcuts import render, redirect


# Create your views here.

# Template error 404
def error404template(request):
    return render(request, "temp_error/404_error.html")


# Template error 500
def error500template(request):
    return render(request, "temp_error/500_error.html")



class Home(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'home.html',context)