from django.test import TestCase
from ..models import Category, Region, Brand

class CategoryModelTest(TestCase):
        
    def test_main_category_creation(self):
        category = Category.objects.create(name="Electronics", is_main=True, slug="electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertTrue(category.is_main)
        self.assertEqual(category.slug, "electronics")
        self.assertIsNone(category.parent)
        
    def test_sub_category_creation(self):
        parent = Category.objects.create(name="Electronics", is_main=True, slug="electronics")
        sub_category = Category.objects.create(name="Mobile Phones", parent=parent, slug="mobile-phones")
        self.assertEqual(sub_category.name, "Mobile Phones")
        self.assertFalse(sub_category.is_main)
        self.assertEqual(sub_category.parent, parent)
        self.assertEqual(sub_category.slug, "mobile-phones")
        self.assertEqual(sub_category.parent, parent)
    
    def test_region_creation(self):
        region = Region.objects.create(name="Istanbul", sorting=8)
        self.assertEqual(region.name, "Istanbul")
        self.assertEqual(region.sorting, 8)
        self.assertIsInstance(region, Region)
    
    def test_brand_creation(self):
        brand = Brand.objects.create(name="Samsung")
        self.assertEqual(brand.name, "Samsung")
        self.assertIsInstance(brand, Brand)