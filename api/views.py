from django.http import JsonResponse

from registry.models import *


def regions(request):
    # Get request params

    # Get objects from database
    try:
        objects = Region.objects.all()
    except:
        status = False
    else:
        status = True

    # Convert queryset to list of dicts
    data = list(objects.values('id', 'region'))

    response = {"ok": status, "data": data}
    return JsonResponse(response)





