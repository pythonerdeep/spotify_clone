from django.db import models

# Create your models here.
class Album(models.Model):
    # id= models.AutoField(primary_key=False)
    album_id = models.CharField(max_length=200)
    album_name= models.CharField(max_length=500)
    album_url= models.URLField(max_length = 200)
    album_label= models.CharField(max_length=1000)
    album_type= models.CharField(max_length=300)
    artist_name=models.CharField(max_length=200)
    total_tracks=models.IntegerField()
    release_date= models.DateField()
    is_new=models.BooleanField(default=False)

    def __str__(self):
        return self.album_id



class Track(models.Model):
    track_id= models.CharField(max_length=200)
    track_name= models.CharField(max_length=1000)
    duration_ms= models.IntegerField()
    artist= models.CharField(max_length=200)
    track_url= models.URLField(max_length=200)
    album= models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.track_name