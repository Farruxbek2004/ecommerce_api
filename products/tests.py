from django.test import TestCase
from django.urls import reverse
from django.test import Client
from common.models import Category, Brand
from products.models import Product

client = Client()


class TestProductList(TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.new_product = None

    def setUp(self) -> None:
        self.brand = Brand.objects.create(title="New Brand")
        self.category = Category.objects.create(title="New Category")
        self.product = Product.objects.create(
            title="New product1", price=10000, category=self.category, brand=self.brand
        )

        new_product = {
            "title": "new, product",
            "price": 100,
            "category": self.category.id,
            "brand": self.brand.id
        }

    def test_product_list(self):
        url = reverse("products_list_create")
        # self.assertEquals(self.product.title, "New product1")
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data["results"][0]["title"], self.product.title, self.product.price)

    def test_product_create(self):
        url = reverse("products_list_create")
        response = client.post(url, data=self.new_product)
        self.assertEquals(response.status_code, 201)
        self.assertNotEquals(response.status_code, 400)
        self.assertEquals(response.data["title"], self.new_product["title"])

    def test_product_detail(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})
        response = client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.product.title, "New product1")

    def test_product_update(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})
        data = {
            "title": "new",
            "price": 20000,
            "category": self.category.id
        }

        response = client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], data["title"])

    def test_product_delete(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)

# import unittest
# import pytest
#
# def student_age(data: dict):
#     return f"Age: {data.get('age')}, Name: {data.get('name')}"
#
#
# def test_age():
#     get_data = {
#         "name": 'Farruxbek',
#         "age": 19
#     }
#     assert student_age(get_data) ==
#
#
# test_age()
