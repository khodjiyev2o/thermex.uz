from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from apps.common.choices import (
    REGION_CHOICES,
    brand_product_dict,
    category_brand_dict,
    category_choices,
    category_choices_translations,
    cities_translations,
    regions_translations,
)
from apps.common.models import City, Occupation, Region
from apps.products.models import Brand, Category, Product


User = get_user_model()


class Command(BaseCommand):
    help = "Populates db with initial data"
    phones = ["+998913665113", "+998975470007"]
    regions = REGION_CHOICES
    translated_regions = regions_translations
    translated_cities = cities_translations

    def handle(self, *args, **options):
        self.super_user()
        self.create_occupations()
        self.create_regions()
        self.create_products()

    def super_user(self):
        self.stdout.write(self.style.SUCCESS("Creating the superusers"))
        for phone in self.phones:
            try:
                User.objects.create_superuser(phone=phone, password="password!")
                self.stdout.write(self.style.SUCCESS('Successfully created super user with phone number "%s"' % phone))
            except IntegrityError:
                self.stdout.write(self.style.ERROR('User phone number "%s" already exists' % phone))

    def create_regions(self):
        self.stdout.write(self.style.SUCCESS("Creating the regions"))
        for region in self.regions.keys():
            region_ru = self.translated_regions[region]
            try:
                new_region = Region.objects.create(name_uz=region, name_ru=region_ru)
                for city in self.regions[region]:
                    try:
                        city_ru = self.translated_cities[region][city]
                        print("city_ru", city_ru)
                        City.objects.create(name_uz=city, region_uz=new_region, name_ru=city_ru, region_ru=new_region)
                    except Exception:
                        City.objects.create(name=city, region=new_region, region_ru=new_region)
                    self.stdout.write(self.style.SUCCESS('Successfully created  "%s"' % city))
            except IntegrityError:
                self.stdout.write(self.style.ERROR('Region "%s" already exists' % region))
        self.stdout.write(self.style.SUCCESS("Finishing the creation of regions"))

    def create_occupations(self):
        self.stdout.write(self.style.SUCCESS("Creating the jobs"))
        jobs = {"Sotuvchi": "Продавец", "Chilangar": "Монтажник"}
        for job in list(jobs.keys()):
            try:
                Occupation.objects.create(name=job, name_ru=jobs[job])
                self.stdout.write(self.style.SUCCESS(f"Created {job} occupation"))
            except IntegrityError:
                self.stdout.write(self.style.ERROR('Error on creating "%s"' % job))
            self.stdout.write(self.style.SUCCESS("Finished creating  the jobs"))

    def create_products(self):
        self.stdout.write(self.style.SUCCESS("Creating the products"))
        for category in category_choices:
            category_instance = Category.objects.create(name=category, name_ru=category_choices_translations[category])
            for brand in category_brand_dict[category]:
                brand_instance = Brand.objects.create(name=brand, category=category_instance)
                for product in brand_product_dict[brand]:
                    Product.objects.create(name=product, brand=brand_instance)
        self.stdout.write(self.style.SUCCESS("Finishing creation of  the products"))
