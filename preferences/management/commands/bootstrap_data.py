from django.core.management.base import BaseCommand
from preferences.models import Entertainment, Dining, OutDoors, StayHome, Preferences

class Command(BaseCommand):
    help = 'Adds Peference options to their respective tables'
    e_ops = [
        'Netflix',
        'Movie Theater',
        'Concert',
        'Local Bar',
        'Ballet',
        'Escape Room',
        'Axe Throwing',
        'Sports Game',
        'Trivia Night',
        'Comedy House'
    ]
    d_ops = [
        'American Cusine',
        'Mexican Cusine',
        'Local Cafe',
        'Diner',
        'Italian Cusine',
        'Steakhouse',
        'Brunch',
        'Desert',
        'Street Food',
        'Thai Cusine'
    ]
    o_ops = [
        'Local Walk',
        'Local Hike',
        'Go to the Lake',
        'Go Swimming',
        'Ride Bikes',
        'Scavenger Hunt',
        'Outdoor fitness class',
        'Community Service',
        'Minigolf / Golfing',
        'Camping'
    ]
    sh_ops = [
        'Clue',
        'Host a Dinner',
        'Bubble Bath',
        'Fire Pit',
        'Massages',
        'Video Game',
        'Something new for dinner',
        'Puzzle',
        'Meditate',
        'Eat by Candle Light'
    ]
    pref_ops = [
        'Entertainment',
        'Dining',
        'Out Doors',
        'Stay At Home'
    ]
    def handle(self, *args, **options):
        for option in self.e_ops:
            new_entertainment = Entertainment.objects.create(
                entertainment_choices=option
            )
        
        for option in self.d_ops:
            new_Dining = Dining.objects.create(
                dining_choices=option
            )
        
        for option in self.o_ops:
            new_outdoor = OutDoors.objects.create(
                outdoor_choices=option
            )
        
        for option in self.sh_ops:
            new_stay_home = StayHome.objects.create(
                stay_home_choices=option
            )

        for option in self.pref_ops:
            new_preferences = Preferences.objects.create(
                choice=option
            )

        self.stdout.write(self.style.SUCCESS('Successfully added Preferences'))