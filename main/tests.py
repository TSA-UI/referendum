from django.test import TestCase, Client
from django.utils import timezone
from .models import MenuItem

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_high_rated_item(self):
        now = timezone.now()
        item = MenuItem.objects.create(
            menu="Chivito Plato",
            category="Sirloin",
            restaurant_name="El Machote",
            image="https://www.cocina-uruguaya.com/base/stock/Recipe/chivito-al-plato/chivito-al-plato_web.jpg",
            city="Central Jakarta",
            price=150000,
            rating=4.1,
            specialized="Mexican",
            takeaway=True,
            delivery=True,
            outdoor=False,
            smoking_area=True,
            wifi=True,
        )
        self.assertTrue(item.rating >= 4.0) 
