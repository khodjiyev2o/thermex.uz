from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.catalogue.models import PrizeProduct
from apps.common.models import BaseModel, City
from apps.users.models import User


class Category(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"), unique=True)

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
        unique_together = ("category", "name")

    def __str__(self):
        return f"{self.name}"


class Product(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"))
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=_("Brand"))
    point = models.PositiveIntegerField(default=1, verbose_name=_("Point"))
    sell_point = models.PositiveIntegerField(default=100, verbose_name=_("Sell Point"))
    photo = models.ImageField(_("Photo"), upload_to="products/%Y/%m", blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        unique_together = ("name", "brand")

    def __str__(self):
        return f"Name: {self.name} Category: {self.brand.category}"


class SoldProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"), related_name="sold_products")
    photo = models.ImageField(upload_to="sold_products/%Y/%m")
    barcode = models.CharField(max_length=15, verbose_name=_("Bar Code"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("City"))

    class Meta:
        verbose_name = _("SoldProduct")
        verbose_name_plural = _("SoldProducts")
        unique_together = ("barcode", "product")

    def __str__(self):
        return f"Name: {self.product} User: {self.user}"


class UserBoughtProduct(BaseModel):
    thermex_product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Thermex Product")
    )
    prize_product = models.ForeignKey(
        PrizeProduct, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Prize Product")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"), related_name="bought_products")

    class Meta:
        verbose_name = _("UserBoughtProducts")
        verbose_name_plural = _("UserBoughtProducts")

    def __str__(self):
        if self.thermex_product:
            return f"Name: {self.thermex_product} User: {self.user}"
        return f"Name: {self.prize_product} User: {self.user}"
