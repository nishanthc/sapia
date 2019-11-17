from django.db import models

# Create your models here.
from django.utils.text import slugify
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(
        "name",
        max_length=1024
    )
    slug = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize()
