from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class City(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_("City"), related_name='regions')

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        unique_together = ('region', 'name')

    def __str__(self):
        return f"{self.name}"


class Occupation(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), unique=True)

    class Meta:
        verbose_name = _('Occupation')
        verbose_name_plural = _('Occupations')

    def __str__(self):
        return f"{self.name}"


class Notification(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    text = models.TextField(verbose_name=_("Title"))
    image = models.ImageField(upload_to='notifications/%Y/%m/', null=True, blank=True)

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title}"
