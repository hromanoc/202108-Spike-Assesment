from django.shortcuts import render
from .forms import DistanceModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
# Create your views here.


def calculateDistance(request):
    # Initialization of values
    form = DistanceModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='deliveryapp')
    distance = None
    destination = None
    origin = None

    if form.is_valid():
        instance = form.save(commit=False)

        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        origin_ = form.cleaned_data.get('origin')
        origin = geolocator.geocode(origin_)

        # origin coordinates
        origin_lat = origin.latitude
        origin_lon = origin.longitude
        pointA = (origin_lat, origin_lon)

        # destination coordinates
        destination_lat = destination.latitude
        destination_lon = destination.longitude
        pointB = (destination_lat, destination_lon)

        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)
        
        instance.distance = distance
        instance.save()

    context = {
        'distance' : distance,
        'origin': origin,
        'destination': destination,
        'form': form,
    }

    return render(request, 'deliveryapp/main.html', context)

def error_404_view(request, exception):
    return render(request,'404.html')