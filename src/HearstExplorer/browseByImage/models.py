from django.db import models

# Create your models here.
class Artifact(models.Model):
    catalog_artifact_id = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image_url = models.URLField(max_length=300)
    lat_long = models.CharField(max_length=50)
    production_date = models.CharField(max_length=75)
    production_date_earliest = models.DateTimeField("Earliest production date")
    production_date_latest = models.DateTimeField("Latest production date")