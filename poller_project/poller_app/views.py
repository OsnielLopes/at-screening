from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")