from django.test import TestCase
from django.urls import resolve
from main.views import index
from products.models import Categories

# Create your tests here.
class HomeIndexTest(TestCase):

    def test_toot_url_resolve_to_index_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/index.html' )

    def test_categories_obfject_index(self):
        response = self.client.get('/')
        print(response)
        categories = Categories.objects.create(name='Creatine', slug='creatine')
        self.assertContains(response, categories.name)