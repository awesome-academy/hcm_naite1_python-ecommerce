from django.test import TestCase
from catalog.models import Order

def test_date_of_death_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('ordered_date').verbose_name
        self.assertEqual(field_label, 'ordered_date')
