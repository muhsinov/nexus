from django.shortcuts import render

def blog(requests):
    return render(requests, 'blog.html')