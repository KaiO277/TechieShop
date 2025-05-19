from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True)  # Có thể là URL hoặc base64
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name