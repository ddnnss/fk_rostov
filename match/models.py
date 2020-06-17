from django.db import models
from team.models import Team
from random import choices
import string

class Match(models.Model):
    team1 = models.ForeignKey(Team, blank=False, null=True, on_delete=models.CASCADE,
                              verbose_name='Команда1', related_name='team1')
    team2 = models.ForeignKey(Team, blank=False, null=True, on_delete=models.CASCADE,
                              verbose_name='Команда2', related_name='team2')
    name_slug = models.CharField(max_length=255,null=True,blank=True,editable=False)
    date = models.DateTimeField('Дата проведения', blank=True, null=True)
    ligue = models.CharField('Лига', max_length=255, default='Премьер Лига')
    place = models.CharField('Место', max_length=255, default='Арена Ростов')
    is_preorder = models.BooleanField('Только предзаказ ?', blank=False, null=True)
    is_active = models.BooleanField('Отображается ?', default=True)

    def save(self, *args, **kwargs):
        self.name_slug = f'{self.team1.name_slug}_vs_{self.team2.name_slug}_{"".join(choices(string.ascii_lowercase + string.digits, k=2))}'
        super(Match, self).save(*args, **kwargs)

    def __str__(self):
        return f'id:{self.id} | {self.date} | Матч : {self.team1.name} - {self.team2.name}'

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"
