from django.test import TestCase
from django.apps import apps

# Imports for app tests
from .apps import ShopConfig

#Imports for views testing
from .models import Product

# Create your tests here.
# Testing the app for the blog section
class TestShopConfig(TestCase):

    def test_shop_app(self):
        self.assertEqual("shop", ShopConfig.name)
        self.assertEqual("shop", apps.get_app_config("shop").name)

#Testing the shop views
class TestShopViews(TestCase):

    def get_shop_home_view(self):
        shop_home = self.client.get("/shop/")
        self.assertEqual(shop_home.status_code, 200)
        self.assertTemplateUsed(shop_home, "shop/home.html")