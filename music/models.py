from django.db import models
from django.conf import settings

class ArtistProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='artist_profile'
    )
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    title = models.CharField(max_length=128, blank=True)
    cover_image = models.ImageField(upload_to='album_covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=128, blank=True)
    audio_file = models.FileField(upload_to='tracks/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')

    def __str__(self):
        return self.title


class ArtistDiscography(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE, related_name='discography')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='artists')

    class Meta:
        unique_together = ('artist', 'album')

    def __str__(self):
        return f"{self.artist.artist_name} - {self.album.title}"
