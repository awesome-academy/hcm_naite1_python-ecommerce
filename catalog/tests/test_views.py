from django.test import TestCase
from django.urls import reverse
from catalog.models import Customer, Order
    
class OrderViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = Customer.objects.create_customer(username='testuser1', password='1q2w3e4r5t6y7u8i9o0p')
        test_user2 = Customer.objects.create_customer(username='testuser2', password='0p9o8i7u6y5t4r3e2w1q')

        test_user1.save()
        test_user2.save()

        test_author = Customer.objects.create(first_name='Oannh', last_name='Le')
        test_order = Order.objects.create(
            ref_code='111',
            status='N',
            shipping_address='241 Go Vap HCM',
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('cart'))
        self.assertRedirects(response, '/accounts/login/?next=/cart')


        # Confirm all books belong to testuser1 and are on loan
        for product in response.context['order']:
            self.assertEqual(response.context['customer'], product.order)
            self.assertEqual(product.status, 'N')
