from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(
        "name",
        max_length=1024
    )

    def __str__(self):
        return self.name.capitalize()
