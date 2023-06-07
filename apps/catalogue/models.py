from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class PrizeParentCategory(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"), unique=True)
    photo = models.ImageField(_("Photo"), upload_to="prize/parent_category/%Y/%m", blank=True, null=True)

    class Meta:
        verbose_name = _("PrizeParentCategory")
        verbose_name_plural = _("PrizeParentCategories")

    def __str__(self):
        return f"{self.name}"


class PrizeChildCategory(BaseModel):
    parent_category = models.ForeignKey(
        PrizeParentCategory, on_delete=models.CASCADE, verbose_name=_("PrizeParentCategory")
    )
    name = models.CharField(max_length=256, verbose_name=_("Name"))
    photo = models.ImageField(_("Photo"), upload_to="prize/child_category/%Y/%m", blank=True, null=True)

    class Meta:
        verbose_name = _("PrizeChildCategory")
        verbose_name_plural = _("PrizeChildCategory")
        unique_together = ("parent_category", "name")

    def __str__(self):
        return f"{self.name}"


class PrizeProduct(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"))
    category = models.ForeignKey(PrizeChildCategory, on_delete=models.CASCADE, verbose_name=_("Category"))
    sell_point = models.PositiveIntegerField(default=100, verbose_name=_("Sell Point"))
    photo = models.ImageField(_("Photo"), upload_to="prize/products/%Y/%m", blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("PrizeProduct")
        verbose_name_plural = _("PrizeProducts")
        unique_together = ("name", "category")

    def __str__(self):
        return f"Name: {self.name} Category: {self.category.name}"
