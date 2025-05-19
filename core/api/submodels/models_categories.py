from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True)  # Có thể là URL hoặc base64

    def __str__(self):
        return self.name