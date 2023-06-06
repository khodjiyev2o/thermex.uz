from modeltranslation.translator import TranslationOptions, translator

from apps.catalogue.models import PrizeChildCategory, PrizeParentCategory, PrizeProduct


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(PrizeParentCategory, CategoryTranslationOptions)


class PrizeChildCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(PrizeChildCategory, PrizeChildCategoryTranslationOptions)


class PrizeProductTranslationOptions(TranslationOptions):
    fields = ("description",)


translator.register(PrizeProduct, PrizeProductTranslationOptions)
