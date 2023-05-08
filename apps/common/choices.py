from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.TextChoices):
    Tashkent = 'Tashkent', _('Tashkent')
    Samarkand = 'Samarkand', _('Samarkand')
    Bukhara = 'Bukhara', _('Bukhara')
    Khiva = 'Khiva', _('Khiva')
    Fergana = 'Fergana', _('Fergana')
    Namangan = 'Namangan', _('Namangan')
    Andijan = 'Andijan', _('Andijan')
    Navoi = 'Navoi', _('Navoi')
    Nukus = 'Nukus', _('Nukus')
    Termez = 'Termez', _('Termez')
    Urgench = 'Urgench', _('Urgench')
    Kokand = 'Kokand', _('Kokand')
    Jizzakh = 'Jizzakh', _('Jizzakh')
    Qarshi = 'Qarshi', _('Qarshi')
    Margilan = 'Margilan', _('Margilan')


class Job(models.TextChoices):
    Sotuvchi = 'Sotuvchi', _('Sotuvchi')
    Chilangar = 'Chilangar', _('Chilangar')


REGION_CHOICES = {
        'tashkent': (
            ('yakkasaray', 'Yakkasaray'),
            ('shaykhontohur', 'Shaykhontohur'),
            ('mirzo ulugbek', 'Mirzo Ulugbek'),
            ('chilonzor', 'Chilonzor'),
            ('yashnabad', 'Yashnabad'),
        ),
        'samarkand': (
            ('samarkand city', 'Samarkand city'),
            ('narpay', 'Narpay'),
            ('urgut', 'Urgut'),
            ('ishtikhan', 'Ishtikhan'),
            ('bulungur', 'Bulungur'),
            ('pakhtachi', 'Pakhtachi'),
            ('kattakurgan', 'Kattakurgan'),
        ),
        'bukhara': (
            ('bukhara city', 'Bukhara city'),
            ('kagan', 'Kagan'),
            ('peshku', 'Peshku'),
            ('romitan', 'Romitan'),
            ('kogon', 'Kogon'),
            ('vobkent', 'Vobkent'),
            ('shofirkon', 'Shofirkon'),
        )
}
