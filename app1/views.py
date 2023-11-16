from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def redbus (request):
    return HttpResponse("Bus Moving")

def nalibus(request):
    return render(request,'page.html')