from django.db import models
from pytils.translit import slugify
from match.models import Match

class Sector(models.Model):
    name = models.CharField('Название сектора', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Sector, self).save(*args, **kwargs)

    def __str__(self):
        return f'Сектор: {self.name}'

    class Meta:
        verbose_name = "Сектор"
        verbose_name_plural = "Сектора"




class Row(models.Model):
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE,blank=False,null=True, verbose_name='Относится к')
    number = models.IntegerField('Номер ряда', blank=False, null=True)

    def __str__(self):
        return f'Ряд {self.number} сектора: {self.sector.name}'

    class Meta:
        verbose_name = "Ряд"
        verbose_name_plural = "Ряды"


class Place(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, blank=False, null=True, verbose_name='Относится к')
    number = models.IntegerField('Номер места', blank=False, null=True)
    is_free = models.BooleanField('Свободно ?', default=True)
    def __str__(self):
        return f'Место {self.number} ряда {self.row.number} сектора {self.row.sector.name}'

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Price(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Матч')
    place = models.ForeignKey(Place,  on_delete=models.CASCADE, blank=True, null=True,verbose_name='Место')
    price = models.IntegerField('Цена билета', blank=False, null=True)

    class Meta:
        verbose_name = "Цена билета"
        verbose_name_plural = "Цены билетов"