
from django.db import models
from django.contrib import admin
class Movies(models.Model):
    NAME=models.CharField(max_length=20)
    PHONE=models.IntegerField()
    Movie_Name=models.CharField(max_length=200)
    Amount=models.IntegerField()
    Genre=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    Rating=models.FloatField(help_text="From '0.0' to '5.0'")
    

class MoviesAdmin(admin.ModelAdmin):
    list_display=('NAME','PHONE','Movie_Name','Amount','Genre','language','Rating')
# Create your models here.
