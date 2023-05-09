
from django.core.management.base import BaseCommand
from django.db.models import Count
from datetime import timedelta, datetime
from django.utils.timezone import utc
from school.models import Student

class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'
  
    def handle(self, *args, **kwargs):
        print("yesssss")
        Student.objects.get_or_create(
            name = 'RAHUL'
        )