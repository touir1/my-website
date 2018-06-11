from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("""
        <h1>Welcome to my website ! </h1>
        <p>this is from the blog home view</p>
    """)

def viewArticle(request, id_article):
    return HttpResponse(
        "we are showing the article with id #{0} !".format(id_article)
    )
