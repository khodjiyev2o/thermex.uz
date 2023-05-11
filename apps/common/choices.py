from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.TextChoices):
    TashkentShahri = 'Tashkent shahri', _('Tashkent shahri')
    ToshkentViloyati = 'Toshkent viloyati', _('Toshkent viloyati')
    Samarkand = 'Samarkand', _('Samarkand')
    Bukhara = 'Bukhara', _('Bukhara')
    Andijon = 'Andijon', _('Andijon')
    Fergana = 'Fergana', _('Fergana')
    Jizzakh = 'Jizzakh', _('Jizzakh')
    Namangan = 'Namangan', _('Namangan')
    Navoi = 'Navoi', _('Navoi')
    Qashqadaryo = 'Qashqadaryo', _('Qashqadaryo')
    Qoraqalpogiston = 'Qoraqalpogiston', _('Qoraqalpogiston')
    Sirdaryo = 'Sirdaryo', _('Sirdaryo')
    Surxondaryo = 'Surxondaryo', _('Surxondaryo')
    Xorazm = 'Xorazm', _('Xorazm')


class Job(models.TextChoices):
    Sotuvchi = 'Sotuvchi', _('Sotuvchi')
    Chilangar = 'Chilangar', _('Chilangar')


REGION_CHOICES = {
        'Tashkent shahri': [
            "Bektemir tumani",
            "Chilonzor tumani",
            "Mirobod tumani",
            "Mirzo Ulugbek tumani",
            "Olmazor tumani",
            "Sergeli tumani",
            "Shayhontohur tumani",
            "Uchtepa tumani",
            "Yakkasaroy tumani",
            "Yashnaobod tumani",
            "Yunusobod tumani",
            ],
        "Toshkent viloyati":[
            "Angren shahri",
            "Bekobod shahri",
            "Bekobod tumani",
            "Boka tumani",
            "Bo'stonliq tumani",
            "Chinoz tumani",
            "Chirchiq shahri",
            "O'rta chirchiq tumani",
            "Ohangaron tumani",
            "Olmaliq shahri",
            "Oqqo'rg'on tumani",
            "Parkent tumani",
            "Piskent tumani",
            "Qibray tumani",
            "Quyi chirchiq tumani",
            "Yangiyo'l tumani",
            "Yuqori chirchiq tumani",
            "Zangiota tumani"],
        'Samarkand': [
            'Bulung\'ur tumani',
            'Ishtixon tumani',
            'Jomboy tumani',
            'Kattaqo\'rg\'on shahri',
            'Kattaqo\'rg\'on tumani',
            'Narpay tumani',
            'Nurobod tumani',
            'Oqdaryo tumani',
            'Past darg\'om tumani',
            'Paxtachi tumani',
            'Poyariq tumani',
            'Qo\'shrabot tumani',
            'Samarqand shahri',
            'Samarqand tumani',
            'Toyloq tumani',
            'Urgut tumani'
        ],
        'Bukhara': [
            'Buxoro shahri',
            'Buhoro tumani',
            "G'ijduvon tumani",
            "Jondor tumani",
            "Kogon tumani",
            "Olot tumani",
            "Peshko tumani",
            "Qorako'l tumani",
            "Qorovulbozor tumani",
            "Romiton tumani",
            "Shofirkon tumani",
            "Vobkent tumani"
        ],
        'Andijon': [
            'Andijon shahri',
            'Andijon tumani',
            'Asaka tumani',
            'Baliqchi tumani',
            "Bo'ston tumani",
            'Buloqboshi tumani',
            'Izboskan tumani',
            'Jalaquduq tumani',
            'Marhamat tumani',
            "Oltinko'l tumani",
            'Pahtaobod tumani',
            "Qo'rgo'ntepa tumani",
            'Shahrixon tumani',
            "Ulug'nor tumani",
            "Xo'jaobod tumani",
            'Xonobod shahri'
        ],
        "Fergana": [
            "Beshariq tumani",
            "Bog'dod tumani",
            "Buvayda tumani",
            "Dang'ara tumani",
            "Farg'ona shahri",
            "Farg'ona tumani",
            "Furqat tumani",
            "Marg'ilon shahri",
            "O'zbekiston tumani",
            "Oltiariq tumani",
            "Qo'qon shahri"	,
            "Qo'shtepa tumani",
            "Quva tumani",
            "Quvasoy shahri",
            "Rishton tumani",
            "So'x tumani",
            "Toshloq tumani",
            "Uchko'prik tumani",
            "Yozyovon tumani"
            ],
        "Jizzakh": [
            'Arnasoy tumani',
            'Baxmal tumani',
            'Do\'stlik tumani',
            'Forish tumani',
            'G\'allaorol tumani',
            'Jizzax shahri',
            'Jizzax tumani',
            'Mirzacho\'l tumani',
            'Paxtakor tumani',
            'Yangiobod tumani',
            'Zafarobod tumani',
            'Zarband tumani',
            'Zomin tumani'],
        "Namangan": [
            'Namangan shahri',
            'Namangan tumani',
            'Chortoq tumani',
            'Chust tumani',
            'Kosonsoy tumani',
            'Mingbuloq tumani',
            'Norin tumani',
            'Pop tumani',
            "To'raqo'rg'on tumani",
            "Uchqo'rg'on tumani",
            "Uychi tumani",
            'Yangiqo\'rgon tumani'],
        "Navoi": [
            'Karmana tumani',
            'Konimex tumani',
            'Navbahor tumani',
            'Navoiy shahri',
            'Nurota tumani',
            'Qiziltepa tumani',
            'Tomdi tumani',
            'Uchquduq tumani',
            'Xatirchi tumani',
            'Zarafshon shahri'
        ],
        "Qashqadaryo": [
            'Karmana tumani',
            'Konimex tumani',
            'Navbahor tumani',
            'Navoiy shahri',
            'Nurota tumani',
            'Qiziltepa tumani',
            'Tomdi tumani',
            'Uchquduq tumani',
            'Xatirchi tumani',
            'Zarafshon shahri'
        ],
        "Qoraqalpogiston": [
            'Amudaryo tumani',
            'Beruniy tumani',
            'Chimboy tumani',
            'Ellikqala tumani',
            'Kegeyli tumani',
            'Mo\'ynoq tumani',
            'Nukus shahri',
            'Nukus tumani',
            'Qonliko\'l tumani',
            'Qorauzaq tumani',
            'Qung\'irot tumani',
            'Shumanay tumani',
            'Taxiatosh shahri',
            'Taxtako\'pir tumani',
            'To\'rtko\'l tumani',
            'Xo\'jayli tumani'
        ],
        "Sirdaryo": [
            'Boyovut tumani',
            'Guliston shahri',
            'Guliston tumani',
            'Oqoltin tumani',
            'Sardoba tumani',
            'Sayxunobod tumani',
            'Shirin shahri',
            'Sirdaryo tumani',
            'Xovos tumani',
            'Yangiyer shahri'
        ],
        "Surxondaryo": [
        "Angor tumani",
        "Bandixon tumani",
        "Boysun tumani",
        "Denov tumani",
        "Jarqo'rg'on tumani",
        "Muzrobot tumani",
        "Oltinsoy tumani",
        "Qiziriq tumani",
        "Qumqo'rg'on tumani",
        "Sariosiyo tumani",
        "Sherobod tumani",
        "Sho'rchi tumani",
        "Termiz shahri",
        "Termiz tumani",
        "Uzun tumani"
    ],
        "Xorazm": [
            'Bog\'ot tumani',
            'Gurlan tumani',
            'Qo\'shko\'pir tumani',
            'Shovot tumani',
            'Urganch shahri',
            'Urganch tumani',
            'Xazorasp tumani',
            'Xiva tumani',
            'Xonqa tumani',
            'Yangiariq tumani',
            'Yangibozor tumani'
        ],
}
