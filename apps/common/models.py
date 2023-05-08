from django.db import models
from .choices import City


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    city = models.CharField(max_length=255, choices=City.choices)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return f"{self.city}"
