from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from django_extensions.db.models import TimeStampedModel


class Product(TimeStampedModel):
    merchant = models.ForeignKey(
        'users.Merchant',
        on_delete=models.CASCADE,
        related_name="products",

    )

    name = models.CharField(
        "name",
        max_length=1024
    )

    description = models.TextField(
        "Description",
        max_length=1024,
        blank=True,
    )

    price = models.IntegerField(
        "price"
    )

    attributes = JSONField(
        blank=True,
        null=True
    )

    category = models.ManyToManyField(
        "category",
        related_name="products",
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    stock = models.IntegerField(
        "stock",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


class Category(TimeStampedModel):
    name = models.CharField(
        "name",
        max_length=1024,
        unique=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False
    )
    parent = models.ForeignKey(
        'category',
        null=True,
        on_delete=models.CASCADE
    )
    primary = models.BooleanField(
        null=True
    )

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})
