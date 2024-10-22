from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache


def hello(request):
    x = 10
    #cache.set("int", x, timeout=20)
    i = cache.get("int")
    return HttpResponse(f"Hello World, {i}")
