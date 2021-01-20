# Generated by Django 2.2.14 on 2021-01-17 13:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Baslik')),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Olusturma Tarihi')),
                ('article_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoqraf Ekle')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admin')),
            ],
        ),
    ]
