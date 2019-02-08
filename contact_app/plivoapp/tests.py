from django.test import TestCase

# Create your tests here.


from django.test import TestCase

# Create your tests here.

from .models import person

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="krishna", phone_no="8318762027")

    def test_startswith(self):
        self.assertEqual(person.objects.filter(filter_name__istartswith='f').count)
