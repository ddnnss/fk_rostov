# Generated by Django 2.2.7 on 2020-06-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отображается ?'),
        ),
    ]
