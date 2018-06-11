from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("""
        <h1>Welcome to my website ! </h1>
        <p>this is from the resume home view</p>
    """)
