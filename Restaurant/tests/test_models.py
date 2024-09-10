from django.test import TestCase
from Restaurant.models import Booking, Menu
from datetime import datetime

class MenuModelTest(TestCase):
    
    def setUp(self):
        self.menu_item = Menu.objects.create(
            Title="Burger",
            Price=9.99,
            Inventory=10
        )
        
    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.Title, "Burger")
        self.assertEqual(self.menu_item.Price, 9.99)
        self.assertEqual(self.menu_item.Inventory, 10)
        
    def test_menu_item_str(self):
        self.assertEqual(str(self.menu_item), "Burger : 9.99 ")
        

class BookingModelTest(TestCase):
    
    def setUp(self):
        self.booking = Booking.objects.create(
            Name="Jonh Doe",
            No_of_guests=2,
            BookingDate=datetime.now()
        )
     
        
    def test_booking_creation(self):
        self.assertEqual(self.booking.Name, "Jonh Doe")
        self.assertEqual(self.booking.No_of_guests, 2)
        self.assertTrue(isinstance(self.booking.BookingDate, datetime))
        
    def test_booking_str(self):
        self.assertEqual(str(self.booking), "Jonh Doe")