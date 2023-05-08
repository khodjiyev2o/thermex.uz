from django.core.management.base import BaseCommand, CommandError
from apps.common.models import Region
from apps.common.choices import City, REGION_CHOICES
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    help = "Populates db with initial data"
    phones = ['+998913665113', '+998975470007']
    regions = REGION_CHOICES
    """add_arguments is used for additional arguments"""
    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.super_user()
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

        for city in self.regions.keys():
            try:
                for region in self.regions[city]:
                    Region.objects.create(city=city, name=region)
                    self.stdout.write(
                        self.style.SUCCESS('Successfully created  "%s"' % region)
                    )
            except IntegrityError:
                self.stdout.write(
                    self.style.ERROR('Error on creating "%s"' % city)
                )
            self.stdout.write(
                self.style.SUCCESS('Finishing the creation of regions')
            )