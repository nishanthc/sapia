from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from shop.models import Category


class Account(AbstractUser):
    company_name = models.CharField(
        "Company Name",
        max_length=100,
        null=True
    )
    website_url = models.CharField(
        "Website URL",
        max_length=1024,
        blank=True,
        null=True
    )

    tel_number = models.CharField(
        "Telephone Number",
        max_length=13,
        null=True
    )
    mob_number = models.CharField(
        "Mobile Number",
        max_length=13,
        null=True,
        blank=True
    )

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
        null=True

    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        null=True
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
        null=True
    )

    city = models.CharField(
        "City",
        max_length=1024,
        null=True
    )

    country = CountryField(
        null=True
    )

    story = models.TextField(
        "Personal Story",
        max_length=1024,
        blank=True
    )

    referral_source = models.TextField(
        "Referral Source",
        max_length=1024,
        blank=True
    )

    def __str__(self):
        return self.email


class Merchant(TimeStampedModel):
    account = models.OneToOneField(
        Account,
        related_name="merchant",
        on_delete=models.CASCADE,

    )
    stockers_count = models.CharField(
        "Stores stocking products",
        max_length=1024,
        null=True
    )

    category = models.ManyToManyField(
        Category,
        related_name="categories",
    )
