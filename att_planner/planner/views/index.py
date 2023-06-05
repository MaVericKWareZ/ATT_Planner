from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse('<h1>Server is Running!</h1>')
