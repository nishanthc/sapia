from shop.models import Category


def categories():
    return {
        'categories': Category.objects.all()
    }
