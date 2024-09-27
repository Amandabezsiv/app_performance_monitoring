from django.http import HttpResponse
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "This is a test endpoint!"})

