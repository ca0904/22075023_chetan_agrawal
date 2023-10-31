from django.db import models

# Create your models here.
class LinkMapping(models.Model):
    original_url = models.URLField(max_length=255)
    hash = models.CharField(max_length=15, unique=True, db_index=True)
    creation_date = models.DateTimeField('creation date')