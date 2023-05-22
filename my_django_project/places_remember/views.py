from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'Universe',
    })


def auth(request):
    return render(request, 'oauth.html')