from django.db import models
from pytils.translit import slugify
from random import choices
import string
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    author = models.CharField('Автор', max_length=255, blank=False, null=True, default='Пресс-служба ФК Ростов')
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Изображение (285 x 150)', upload_to='blog/', blank=False, null=True)
    description = RichTextUploadingField('Статья', blank=True, null=True)
    views = models.IntegerField('Просмотров', blank=True, default=0)
    is_active = models.BooleanField('Отображается на сайте?', default=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = Post.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'Статья : {self.name} '

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ''

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"