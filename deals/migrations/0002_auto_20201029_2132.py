# Generated by Django 2.2.6 on 2020-10-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, help_text='Хелп для image', null=True, upload_to='tasks/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, help_text='Хелп для slug', max_length=100, unique=True, verbose_name='Слаг'),
        ),
    ]