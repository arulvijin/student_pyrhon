from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import profile


# Create your views here.
def demo(request):
    obj=place.objects.all()
    bv = profile.objects.all()
    return render(request,"avindex.html",{'result':obj,'solution':bv})
# def av(program):
#
#     return render(program,"avindex.html",{'solution':bv})


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int( request.GET['num2'])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request, "2.html", {"result": res,"subtract":sub,"multiplication":mul,"division":div})


# def name(request):
#     return render(request,"3.html")
# def vijin(request):
#     return render(request,"4.html")
#
# def final(request):
#     return HttpResponse("i am finshed")