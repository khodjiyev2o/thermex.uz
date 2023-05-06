from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.TextChoices):
    Tashkent = 'tashkent', _('Tashkent')
    Samarkand = 'samarkand', _('Samarkand')
    Bukhara = 'bukhara', _('Bukhara')
    Khiva = 'khiva', _('Khiva')
    Fergana = 'fergana', _('Fergana')
    Namangan = 'namangan', _('Namangan')
    Andijan = 'andijan', _('Andijan')
    Navoi = 'navoi', _('Navoi')
    Nukus = 'nukus', _('Nukus')
    Termez = 'termez', _('Termez')
    Urgench = 'urgench', _('Urgench')
    Kokand = 'kokand', _('Kokand')


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
