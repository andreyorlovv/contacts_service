from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


# Create your models here.
class Contact(models.Model):

    regions = [
        ('DVFO', 'ДВФО'),#
        ('MMO', 'Москва и МО'),#
        ('PFO', 'ПФО'),#
        ('SZFO', 'СЗФО'),
        ('SKFO', 'СКФО'),#
        ('SFO', 'СФО'),
        ('UFO', 'УФО'),
        ('CFO', 'ЦФО'),
        ('YFO', 'ЮФО')
    ]

    title = models.CharField(max_length=255, verbose_name='Название')
    inn = models.PositiveBigIntegerField(verbose_name='ИНН')
    kpp = models.CharField(max_length=255, null=True, blank=True, verbose_name='КПП')

    region = models.CharField(choices=regions, null=True, blank=True, max_length=255, verbose_name='Федеральный округ')

    phones = ArrayField(
        models.CharField(max_length=20, blank=True), size=20, null=True, blank=True, verbose_name='Телефоны'
    )
    email = ArrayField(
        models.CharField(max_length=60, blank=True), size=20, null=True, blank=True, verbose_name='Адреса эл.почт'
    )

    director = models.CharField(max_length=255, null=True, blank=True, verbose_name='Директор или иной представитель')

    def __str__(self):
        return self.title + ' - ' + str(self.inn)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
