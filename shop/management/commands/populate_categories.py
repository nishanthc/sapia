from collections import Set

from django.core.management.base import BaseCommand, CommandError

from shop.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        f = open(dir_path + "/data/categories.txt", "r")
        for x in f:
            categories = [category.strip() for category in x.split('>')]
            for n, category in enumerate(categories):
                if n == 0:
                    if not Category.objects.filter(name=category).exists():
                        new_category = Category()
                        new_category.name = category
                        new_category.primary = True
                        new_category.save()
                        print(category)
                else:
                    if not Category.objects.filter(name=category).exists():
                        parent_category = Category.objects.get(name=categories[n - 1])
                        new_category = Category()
                        new_category.name = category
                        new_category.parent = parent_category
                        new_category.save()
                        print(category)
