# Generated by Django 2.1.1 on 2019-11-17 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('users', '0002_auto_20191117_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchaser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='purchasers', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='purchasers', to='shop.Category')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='merchant',
            name='category',
            field=models.ManyToManyField(related_name='merchants', to='shop.Category'),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='store_type',
            field=models.ManyToManyField(related_name='purchasers', to='users.StoreType'),
        ),
    ]