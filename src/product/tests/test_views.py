from django.test import TestCase
from ..views import product, detail, product_add
from category.models import Category, Region, Brand
from user.models import Profile
from ..models import Product, ProductImage
from django.contrib.auth.models import User

class ProductViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, first_name="Test", last_name="User", phone_number="1234567890")
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.region = Region.objects.create(name="Test Region", sorting=1)
        self.brand = Brand.objects.create(name="Test Brand")
        self.product = Product.objects.create(
            title="Test Product",
            description="This is a test product.",
            location=self.region,
            category=self.category,
            brand=self.brand,
            user=self.profile,
            condition=1,
            status=1,
            price=100,
            price_on_call=False,
        )
        
    def test_product_view(self):
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertContains(response, "Test Category")
        self.assertContains(response, "Test Region")
        self.assertContains(response, "Test Brand")
        self.assertContains(response, "100")
        self.assertContains(response, "Test User")
        self.assertContains(response, "1234567890")
        self.assertContains(response, "New")
    
        # def test_product_detail_view(self):
def dummy(x):
    return x

class CheckDummy(TestCase):
    def test_case_dummy(self):
        x = 10
        first = dummy(x)
        second = dummy(x)
        self.assertIs(first, second)
            
        