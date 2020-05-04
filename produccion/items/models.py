from django.db import models

# Create your models here.
# items.models
from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    summary = models.TextField(max_length=5000,null=True)
    poster_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(
				max_length=50, null=True,blank =True, unique=True)

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return self.name
