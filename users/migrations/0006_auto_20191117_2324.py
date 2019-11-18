# Generated by Django 2.1.1 on 2019-11-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191117_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referralsource',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='storetype',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='referralsource',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storetype',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]