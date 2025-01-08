from django.db import models

# Create your models here.
class Logo(models.Model):
    logo = models.ImageField(upload_to='branding/')

    def __str__(self):
        return "Main Logo"
    class Meta:
        verbose_name_plural = "Logos"
        verbose_name = "Logo"