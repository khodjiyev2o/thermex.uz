from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=255,  verbose_name=_("Name"), unique=True)

    def __str__(self):
        return f"{self.name}"


class City(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    region = models.ForeignKey(Region, on_delete=models.CASCADE,  verbose_name=_("City"), related_name='regions')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        unique_together = ('region', 'name')

    def __str__(self):
        return f"{self.name}"
