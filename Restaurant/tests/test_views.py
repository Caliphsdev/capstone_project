from django.urls import reverse
from rest_framework.test import APITestCase
from Restaurant.models import Booking, Menu
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework import status


class BookingViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.booking = Booking.objects.create(
            Name="Alice", 
            No_of_guests=4, 
            BookingDate=datetime.now()
        )
        
    def test_create_booking(self):
        data = {
            "Name": "Bob",
            "No_of_guests": 3,
            "BookingDate": datetime.now()
        }
        response = self.client.post(reverse('booking'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
    
class MenuViewTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.menu_item = Menu.objects.create(Title="Pizza", Price=12.99, Inventory=20)
        self.client.login(username='testuser', password='testpass')
        
    def test_get_menu_items(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_create_menu_item(self):
        data = {
            "Title": "Pasta",
            "Price": 15.00,
            "Inventory": 30
        }
        response = self.client.post(reverse('menu'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        
    def test_get_single_menu_item(self):
        url = reverse('single_menu', kwargs={'pk': self.menu_item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Title'], "Pizza")
        
    def test_update_menu_item(self):
        data= {
            "Title": "Updated Pizza",
            "Price": 14.99,
            "Inventory": 25
        }
        url = reverse('single_menu', kwargs={'pk': self.menu_item.pk})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(self.menu_item.Title, "Updated Pizza")
        self.assertEqual(str(self.menu_item.Price), str(14.99))
        
    def test_delete_menu_item(self):
        """Test DELETE request to remove a menu item"""
        url = reverse('single_menu', kwargs={'pk': self.menu_item.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)