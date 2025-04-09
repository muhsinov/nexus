from django.test import TestCase
from ..models import Product, ProductImage
from category.models import Category, Region, Brand
from user.models import Profile
from django.contrib.auth.models import User

class ProductModelTestCase(TestCase):
    def test_product_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product.",
            location=Region.objects.create(name="Test Region", sorting=1),
            category=Category.objects.create(name="Test Category", slug="test-category"),
            brand=Brand.objects.create(name="Test Brand"),
            user=Profile.objects.create(first_name="testuser", user=user, phone_number="1234567890"),
            condition=1,
            status=1,
            price=100,
            price_on_call=False,
        )
        self.assertEqual(product.title, "Test Product")
        self.assertEqual(product.description, "This is a test product.")
        self.assertIsInstance(product.location, Region)
        self.assertIsInstance(product.category, Category)
        self.assertIsInstance(product.brand, Brand)
        self.assertIsInstance(product.user, Profile)
        self.assertEqual(product.condition, 1)
        self.assertEqual(product.status, 1)
        self.assertEqual(product.price, 100)
        self.assertFalse(product.price_on_call)
        self.assertIsInstance(product, Product)
        self.assertIsNotNone(product.created_at)
        self.assertIsNotNone(product.updated_at)
        self.assertEqual(product.get_condition(), "New")
        self.assertEqual(str(product), "Test Product")
        
    def test_product_image_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product.",
            location=Region.objects.create(name="Test Region", sorting=1),
            category=Category.objects.create(name="Test Category", slug="test-category"),
            brand=Brand.objects.create(name="Test Brand"),
            user=Profile.objects.create(first_name="testuser", user=user, phone_number="1234567890"),
            condition=1,
            status=1,
            price=100,
            price_on_call=False,
        )
        product_image = ProductImage.objects.create(
            image='path/to/image.jpg',
            product=product,
        )
        self.assertIsInstance(product_image, ProductImage)
        self.assertEqual(product_image.product, product)
        self.assertEqual(product_image.image, 'path/to/image.jpg')
        