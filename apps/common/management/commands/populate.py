from django.core.management.base import BaseCommand
from apps.common.models import Region, City, Occupation
from apps.common.choices import REGION_CHOICES, Job, regions_translations, cities_translations
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    help = "Populates db with initial data"
    phones = ['+998913665113', '+998975470007']
    regions = REGION_CHOICES
    translated_regions = regions_translations
    translated_cities = cities_translations

    """add_arguments is used for additional arguments"""
    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.super_user()
        self.create_occupations()
        self.create_regions()

    def super_user(self):
        self.stdout.write(
            self.style.SUCCESS('Creating the superusers')
        )
        for phone in self.phones:
            try:
                User.objects.create_superuser(phone=phone, password='password!')
                self.stdout.write(
                    self.style.SUCCESS('Successfully created super user with phone number "%s"' % phone)
                )
            except IntegrityError:
                self.stdout.write(
                    self.style.ERROR('User phone number "%s" already exists' % phone)
                )

    def create_regions(self):
        self.stdout.write(
            self.style.SUCCESS('Creating the regions')
        )
        i = 0
        for region in self.regions.keys():
            region_ru = self.translated_regions[region]
            print("region_ru", region_ru)
            try:
                new_region = Region.objects.create(name=region, name_ru=region_ru)
                for city in self.regions[region]:
                    i += 1
                    try:
                        city_ru = self.translated_cities[region][city]
                        print("city_ru", city_ru)
                        City.objects.create(name=city, region=new_region, name_ru=city_ru, region_ru=new_region)
                    except Exception as e:
                        City.objects.create(name=city, region=new_region, region_ru=new_region)
                    self.stdout.write(
                        self.style.SUCCESS('Successfully created  "%s"' % city)
                    )
            except IntegrityError:
                    self.stdout.write(
                        self.style.ERROR('Region "%s" already exists' % region)
                    )
        self.stdout.write(
                self.style.SUCCESS('Finishing the creation of regions')
        )
        print("number of regions", i)

    def create_occupations(self):
        self.stdout.write(
            self.style.SUCCESS('Creating the jobs')
        )
        jobs = {
            'Sotuvchi': 'Продавец',
            'Chilangar': 'Монтажник'
        }
        for job in list(jobs.keys()):
            try:
                Occupation.objects.create(name=job, name_ru=jobs[job])
                self.stdout.write(
                    self.style.SUCCESS(f'Created {job} occupation')
                )
            except IntegrityError:
                self.stdout.write(
                    self.style.ERROR('Error on creating "%s"' % job)
                )
            self.stdout.write(
                self.style.SUCCESS('Finished creating  the jobs')
            )