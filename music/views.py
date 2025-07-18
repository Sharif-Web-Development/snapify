from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def album_page(request):
    context = {
            "user": {
                "name": "Twenty-one Pilots",
                "is_authenticated": True
                },
            }
    return render(request, 'music/album.html', context=context)
