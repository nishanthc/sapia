# Generated by Django 2.1.11 on 2019-11-19 19:00

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191118_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='account',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='account',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='referral_source',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='users.ReferralSource'),
        ),
        migrations.AlterField(
            model_name='account',
            name='tel_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Telephone Number'),
        ),
        migrations.AlterField(
            model_name='account',
            name='zip_code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='ZIP / Postal code'),
        ),
    ]