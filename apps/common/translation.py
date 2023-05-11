from modeltranslation.translator import translator, TranslationOptions
from apps.common.models import Region, City


class RegionTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Region, RegionTranslationOptions)


class CityTranslationOptions(TranslationOptions):
    fields = ('name', 'region', )


translator.register(City, CityTranslationOptions)
