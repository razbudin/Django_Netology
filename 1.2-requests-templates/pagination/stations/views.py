from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_station = []
    with open('data-752-2024-07-29.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            bus_station.append(row)
    paginator = Paginator(bus_station, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
