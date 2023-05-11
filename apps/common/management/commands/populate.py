from django.core.management.base import BaseCommand
from apps.common.models import Region, City, Occupation
from apps.common.choices import REGION_CHOICES, Job
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from googletrans import Translator
User = get_user_model()


class Command(BaseCommand):
    help = "Populates db with initial data"
    phones = ['+998913665113', '+998975470007']
    regions = REGION_CHOICES
    translator = Translator()
    """add_arguments is used for additional arguments"""
    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.super_user()
        self.create_regions()
        self.create_occupations()

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
        for region in self.regions.keys():
            region_ru = self.translator.translate(region, dest='ru')
            new_region = Region.objects.create(name=region, name_ru=region_ru.text)
            for city in self.regions[region]:
                try:
                    city_ru = self.translator.translate(city, dest='ru')
                    City.objects.create(name=city, region=new_region, name_ru=city_ru.text)
                except Exception as e:
                    City.objects.create(name=city, region=new_region)
                self.stdout.write(
                    self.style.SUCCESS('Successfully created  "%s"' % city)
                )
        self.stdout.write(
                self.style.SUCCESS('Finishing the creation of regions')
        )

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