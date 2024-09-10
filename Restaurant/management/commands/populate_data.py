from django.core.management.base import BaseCommand
from faker import Faker
from  Restaurant.models import Booking, Menu
import random

class Command(BaseCommand):
    help = "Populate the database with fake data"
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Populate Booking model
        for _ in range(10): #Creating 10 fake Booking entries
            Booking.objects.create(
                Name=fake.name(),
                No_of_guests=random.randint(1, 10),
                BookingDate=fake.date_time_this_year().isoformat(),
            )
            
        for _ in range(10):
            Menu.objects.create(
               Title=fake.word(),
               Price=round(random.uniform(5.0, 100.0), 2),
               Inventory=random.randint(1, 100), 
            )
            
        self.stdout.write(self.style.SUCCESS("Successfully populated database with fake data"))