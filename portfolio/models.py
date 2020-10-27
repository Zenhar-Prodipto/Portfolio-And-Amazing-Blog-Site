from django.db import models

# Create your models here.


class Web_Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=300)
    image = models.ImageField(
        default="portfolio/images/logo.png", upload_to="portfolio/images/"
    )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class ML_Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=300)
    image = models.ImageField(
        default="portfolio/images/logo.png", upload_to="portfolio/images/"
    )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title