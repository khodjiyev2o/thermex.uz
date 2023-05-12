from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from apps.users.models import User


class Category(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.name}"


class Brand(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    name = models.CharField(max_length=256, verbose_name=_("Brand"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brand")
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name}"


class Product(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"))
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=_("Brand"))
    point = models.PositiveIntegerField(default=1, verbose_name=_("Point"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        unique_together = ('name', 'brand')

    def __str__(self):
        return f"Name: {self.name} Category: {self.brand.category}"


class SoldProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='sold_products')

    class Meta:
        verbose_name = _("SoldProduct")
        verbose_name_plural = _("SoldProducts")

    def __str__(self):
        return f"Name: {self.product} User: {self.user}"
