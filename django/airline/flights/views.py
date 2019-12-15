from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Flight

def index(request):
    context = {
        "flights" : Flight.objects.all()
    }
    return render(request,"flights/index.html",context)

def flight(request,flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context2 = {
        "flight" : flight
    }
    return render(request,"flights/flight.html",context2)