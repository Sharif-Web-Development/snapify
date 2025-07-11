from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def album_page(request):
    return render(request, 'music/album.html', context={"user": "SERJ"})
