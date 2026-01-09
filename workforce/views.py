from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Workforce Management Backend is running",
        "docs": "/swagger/",
        "admin": "/admin/"
    })
