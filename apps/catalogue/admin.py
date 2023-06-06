from django.contrib import admin

from .models import PrizeChildCategory, PrizeParentCategory, PrizeProduct


admin.site.register(PrizeProduct)
admin.site.register(PrizeParentCategory)
admin.site.register(PrizeChildCategory)
