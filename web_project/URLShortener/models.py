from django.db import models

# Create your models here.

# Here the schema is for a Relational Data Model (SQL)
class URL(models.Model):
    originalUrl = models.URLField()
    shortUrl = models.CharField(max_length=200)
