from django.core.management.base import BaseCommand, CommandError
from apps.common.models import Region
from apps.common.choices import City
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    help = "Populates db with initial data"
    phones = ['+998913665113', '+998975470007']

    """add_arguments is used for additional arguments"""
    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.super_user()
        self.regions()

    def super_user(self):
        self.stdout.write(
            self.style.SUCCESS('Creating the superusers')
        )
        for phone in self.phones:
            try:
                User.objects.create(phone=phone, password='password!')
                self.stdout.write(
                    self.style.SUCCESS('Successfully created super user with phone number "%s"' % phone)
                )
            except IntegrityError:
                self.stdout.write(
                    self.style.ERROR('User phone number "%s" already exists' % phone)
                )

    def regions(self):
        self.stdout.write(
            self.style.SUCCESS('Creating the regions')
        )

        for region in self.regions:
            try:
                #User.objects.create(phone=phone, password='password!')
                self.stdout.write(
                    self.style.SUCCESS('Successfully created super user with phone number "%s"' % phone)
                )
            except IntegrityError:
                self.stdout.write(
                    self.style.ERROR('User phone number "%s" already exists' % phone)
                )
