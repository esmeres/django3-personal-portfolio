from django.shortcuts import render
from django.http import HttpResponse


def utilities(request):
    return render(request, 'utilities/utilities.html')
