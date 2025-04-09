# from django.test import TestCase
# from ..forms import CategoryForm, RegionForm, BrandForm

# class CategoryFormTest(TestCase):
#     def test_valid_form(self):
#         form_data = {
#             'name': 'Electronics',
#             'is_main': True,
#             'slug': 'electronics'
#         }
#         form = CategoryForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         self.assertEqual(form.cleaned_data['name'], 'Electronics')
#         self.assertTrue(form.cleaned_data['is_main'])
#         self.assertEqual(form.cleaned_data['slug'], 'electronics')
    
#     def test_invalid_form(self):
#         form_data = {
#             'name': '',
#             'is_main': True,
#             'slug': ''
#         }
#         form = CategoryForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('name', form.errors)
#         self.assertIn('slug', form.errors)

    