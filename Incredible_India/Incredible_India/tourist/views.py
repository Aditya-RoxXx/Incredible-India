from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import City, CityDescription
from .forms import CityDescriptionForm

# Create your views here.
def index(request):
    latest_city_list = City.objects.order_by("-pub_date")[:5]
    context = {"latest_city_list": latest_city_list}
    return render(request, "tourist/index.html", context)

def detail(request, city_id):

    city = get_object_or_404(City, pk=city_id)
    city_description = CityDescription.objects.filter(name=city).first()
    if request.method == 'POST':
        form = CityDescriptionForm(request.POST)
        
        if form.is_valid():
            city_description = form.save(commit=False)
            city_description.name = city
            city_description.save()
            return redirect('tourist:success')
    else:
        form = CityDescriptionForm()

    context = {
        'city': city,
        'city_description': city_description,
        'form': form,
    }
    return render(request, 'tourist/detail.html', context)

def results(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    city_descriptions = CityDescription.objects.filter(name=city)

    context = {
        'city': city,
        'city_descriptions': city_descriptions,
    }
    return render(request, 'tourist/results.html', context)

def city_descriptions(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    descriptions = CityDescription.objects.filter(name=city)

    context = {
        'city': city,
        'descriptions': descriptions,
    }
    return render(request, 'tourist/city_descriptions.html', context)

def success(request):
    return render(request, 'tourist/success.html')

