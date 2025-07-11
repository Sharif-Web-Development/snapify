from django.contrib import admin
from .models import (ArtistProfile,
                     Album,
                     ArtistDiscography,
                     Track)

# Register your models here.
admin.site.register(ArtistProfile)
admin.site.register(ArtistDiscography)
admin.site.register(Album)
admin.site.register(Track)
