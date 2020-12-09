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

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     image = Image.open(self.image.path)
    #     if image.height > 300 or image.width > 300:
    #         output_size = (300, 300)
    #         image.thumbnail(output_size)
    #         image.save(self.image.path)


class ML_Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=300)
    image = models.ImageField(
        default="portfolio/images/logo.png", upload_to="portfolio/images/"
    )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     image = Image.open(self.image.path)
    #     if image.height > 300 or image.width > 300:
    #         output_size = (300, 300)
    #         image.thumbnail(output_size)
    #         image.save(self.image.path)