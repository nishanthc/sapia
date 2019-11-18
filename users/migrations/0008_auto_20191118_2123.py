# Generated by Django 2.1.11 on 2019-11-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_merchant_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='slug',
            field=models.SlugField(blank=True, default='no-slug', unique=True),
            preserve_default=False,
        ),
    ]