from django.db import models
from pytils.translit import slugify

class Team(models.Model):
    name = models.CharField('Название команды',max_length=255, blank=False, null=True, )
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    icon = models.ImageField('Логотип команды', upload_to='team/logo/', blank=False, null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return f'Клуб {self.name}'

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


class TeamMember(models.Model):
    GOALKEEPER = 'GK'
    DEFENDER = 'DF'
    SUBDEFENDER = 'SD'
    ATTACK = 'AT'

    MEMBER_TYPE_CHOICES = [
        (GOALKEEPER, 'Вратарь'),
        (DEFENDER, 'Защитник'),
        (SUBDEFENDER, 'Полузащитник'),
        (ATTACK, 'Нападающий'),
    ]

    team = models.ForeignKey(Team,blank=False, on_delete=models.CASCADE, null=True,verbose_name='В составе')
    fio = models.CharField('ФИО', max_length=255, blank=False, null=True, )
    photo = models.ImageField('Фото', upload_to='team/member/', blank=False, null=True)
    number = models.CharField('Номер', max_length=255, blank=False, null=True, )
    amplua = models.CharField('Амплуа', max_length=2, choices=MEMBER_TYPE_CHOICES, default=GOALKEEPER)
    birthday = models.DateField('День рождения', max_length=255, blank=False, null=True, )
    nationality = models.CharField('Гражданство', max_length=255, blank=False, null=True, )
    height = models.IntegerField('Рост', blank=False, null=True, )
    weight = models.IntegerField('Вес', blank=False, null=True, )
    start_play = models.DateField('Перешел', max_length=255, blank=False, null=True, )
    info = models.TextField('Описание', blank=False, null=True, )

    def __str__(self):
        return f'Игрок: {self.fio}. В составе {self.team.name}'

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

