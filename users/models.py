from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from shop.models import Category


class NameMixin(models.Model):
    name = models.CharField(
        "name",
        max_length=1024
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name.capitalize()


class ReferralSource(NameMixin, TimeStampedModel):
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['order']


class Account(AbstractUser):
    company_name = models.CharField(
        "Company Name",
        max_length=100,
        null=True,
        blank=True
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
        null=True,
        blank=True
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
        null=True,
        blank=True

    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        null=True,
        blank=True
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
        null=True,
        blank=True
    )

    city = models.CharField(
        "City",
        max_length=1024,
        null=True,
        blank=True
    )

    country = CountryField(
        null=True,
        blank=True
    )

    story = models.TextField(
        "Personal Story",
        max_length=1024,
        blank=True,
    )

    referral_source = models.OneToOneField(
        ReferralSource,
        related_name="accounts",
        on_delete=models.CASCADE,
        null=True,
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

    store_name = models.CharField(
        "Store name",
        max_length=1024,
        null=True
    )

    store_description = models.CharField(
        "Store description",
        max_length=1024,
        null=True
    )

    category = models.ManyToManyField(
        Category,
        related_name="merchants",
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.store_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('merchant-detail', kwargs={'slug': self.slug})


class StoreType(NameMixin, TimeStampedModel):
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['order']


class Purchaser(TimeStampedModel):
    account = models.OneToOneField(
        Account,
        related_name="purchaser",
        on_delete=models.CASCADE,

    )
    store_type = models.ManyToManyField(
        StoreType,
        related_name="purchasers",
    )

    category = models.ManyToManyField(
        Category,
        related_name="purchasers",
    )
