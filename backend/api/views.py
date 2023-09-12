import json
from django.http import JsonResponse, HttpRequest


def api_home(request: HttpRequest, *args, **kwargs):
    data = {}
    try:
        data = json.loads(request.body)  # Semelhante ao JSON.parse do Js
        print(json.dumps(request.GET))  # Semelhante ao JSON.stringify do Js
    except:
        pass
    print(data)
    return JsonResponse(data)
