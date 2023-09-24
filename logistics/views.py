import json, math
from django.shortcuts import render
from .models import CoalStock, Railway
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def railway_siding_list(request):
    sidings = CoalStock.objects.all()
    return render(request, 'railway_siding_list.html', {'sidings': sidings})

def homepage(request):
    railway = Railway.objects.all()
    return render(request, 'homepage.html', {'railway': railway})

def map_view(request):
    railway = list(Railway.objects.values("name","location"))
    # sidings = CoalStock.objects.all()
    sidings = list(CoalStock.objects.values("name","location","capacity","available_space","last_updated"))
    return render(request, 'map.html', {'sidings': sidings, 'railway': railway})

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            rake_name = data.get('rake_name', None)
            if rake_name is not None:
                rake = Railway.objects.get(name=rake_name)
                sidings = CoalStock.objects.filter(available_space__gte=int(rake.capacity))
                points = []
                for x in sidings:
                    coordinates = (x.location.split(',')[0], x.location.split(',')[1])
                    points.append(coordinates)
                current = (rake.location.split(',')[0], rake.location.split(',')[1])
                nearest_point = min(points, key=lambda point: haversine(float(current[0]), float(current[1]), float(point[0]), float(point[1])))
                index = points.index(nearest_point)
                siding = sidings[index]
                return JsonResponse({'name': f'{siding.name}', 'location': siding.location, 'available_space': f'{siding.available_space}'})
            else:
                return JsonResponse({'error': 'Invalid or missing rake_name field'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'This is not a POST request'}, status=405)


def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    R = 6371.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
