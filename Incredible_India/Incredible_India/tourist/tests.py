from django.test import TestCase
from django.urls import reverse, resolve
from . import views
from django.contrib.auth import get_user_model
from .models import City, CityDescription
from django.utils import timezone

# Create your tests here.
class CityModelTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            city_name = "Mumbai",
            city_state = "Maharastra",
            pub_date = timezone.now()
        )
    def test_city_creation(self):
        self.assertEqual(self.city.city_name, "Mumbai")
        self.assertEqual(self.city.city_state, "Maharastra")

class CityDescriptionModelTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            city_name = "Mumbai",
            city_state = "Maharastra",
            pub_date = timezone.now()
        )
        self.description = CityDescription.objects.create(
            name = self.city,
            city_description = "A vibrant city with lots of culture.",
            best_food = "Vada Pav",
            best_place_to_visit = "Gateway of India",
            rating = 5
        )

    def test_city_description_creation(self):
        self.assertEqual(self.description.name, self.city)
        self.assertEqual(self.description.city_description, "A vibrant city with lots of culture.")
        self.assertEqual(self.description.best_food, "Vada Pav")
        self.assertEqual(self.description.best_place_to_visit, "Gateway of India")
        self.assertEqual(self.description.rating, 5)

class ViewTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            city_name = "Mumbai",
            city_state = "Maharastra",
            pub_date = timezone.now()
        )
        self.description = CityDescription.objects.create(
            name = self.city,
            city_description = "A vibrant city with lots of culture.",
            best_food = "Vada Pav",
            best_place_to_visit = "Gateway of India",
            rating = 5
        )
        self.url = reverse('tourist:detail', args=[self.city.id])

    def test_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mumbai")
        self.assertContains(response, "A vibrant city with lots of culture.")

    def test_results_view(self):
        url = reverse('tourist:results', args=[self.city.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mumbai")
        self.assertContains(response, "Gateway of India")

    def test_city_descriptions_view(self):
        url = reverse('tourist:city_descriptions', args=[self.city.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mumbai")
        self.assertContains(response, "A vibrant city with lots of culture.")

class UrlsTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            city_name = "Mumbai",
            city_state = "Maharastra",
            pub_date = timezone.now()
        )
    def test_urls(self):
        url = reverse('tourist:index')
        self.assertEqual(resolve(url).func, views.index)

        url = reverse('tourist:detail', args=[self.city.id])
        self.assertEqual(resolve(url).func, views.detail)

        url = reverse('tourist:results', args=[self.city.id])
        self.assertEqual(resolve(url).func, views.results)

        url = reverse('tourist:city_descriptions', args=[self.city.id])
        self.assertEqual(resolve(url).func, views.city_descriptions)

        url = reverse('tourist:success')
        self.assertEqual(resolve(url).func, views.success)