from modeltranslation.translator import TranslationOptions, translator

from apps.products.models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Category, CategoryTranslationOptions)
