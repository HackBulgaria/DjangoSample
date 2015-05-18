from django.test import TestCase
from django.test import Client
from .models import Movie


class WebSiteTests(TestCase):

    def setUp(self):
        self.lotr = Movie.objects.create(
            name="LOTR",
            rating=10,
            type=1,
        )

    def test_show_all_movies(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.lotr.name)
