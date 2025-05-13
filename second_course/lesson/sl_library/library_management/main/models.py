from django.db import models


from django.db import models


# Umumiy abstract model
class MediaItem(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media/images/", null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Book(MediaItem):
    pages = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Journal(MediaItem):
    pages = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journals"


class DigitalMedia(MediaItem):
    file_format = models.CharField(max_length=50)
    file_size = models.FloatField(help_text="Size in MB")
    url = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Digital Media"
        verbose_name_plural = "Digital Media"


class Notifications(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        default="unread",
        choices=[("unread", "Unread"), ("read", "Read")],
    )

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.title
