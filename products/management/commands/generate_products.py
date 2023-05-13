from django.core.management.base import BaseCommand
from faker import Faker

from common.models import Category
from products.models import Product


class Command(BaseCommand):
    help = 'Generate products'

    def handle(self, *args, **options):
        # ProductFactory.create_batch(size=200)
        faker = Faker()
        for _ in range(100):
            category = Category.objects.filter(parent__isnull=True).order_by("?").first()
            Product.objects.create(title=faker.word(), price=1000, category_id=category.id)
        self.stdout.write(self.style.SUCCESS('Successfully generated products.'))

# https://fakestoreapi.com/
