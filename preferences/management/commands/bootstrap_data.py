from django.core.management.base import BaseCommand
from django.utils import timezone
from preferences.models import Entertainment, Dining, OutDoors, StayHome, Preferences
from users.models import User
from dates.models import DatesNightModel
from notifications.models import Notification

import datetime
import random
from mimesis import Generic, Address, Datetime as DT
from mimesis import Text


generic = Generic('en')
text = Text('en')
address = Address()
d_time = DT()


class Command(BaseCommand):
    help = "Adds Peference options to their respective tables"
    e_ops = [
        "Netflix",
        "Movie Theater",
        "Concert",
        "Local Bar",
        "Ballet",
        "Escape Room",
        "Axe Throwing",
        "Sports Game",
        "Trivia Night",
        "Comedy House",
    ]
    d_ops = [
        "American Cusine",
        "Mexican Cusine",
        "Local Cafe",
        "Diner",
        "Italian Cusine",
        "Steakhouse",
        "Brunch",
        "Desert",
        "Street Food",
        "Thai Cusine",
    ]
    o_ops = [
        "Local Walk",
        "Local Hike",
        "Go to the Lake",
        "Go Swimming",
        "Ride Bikes",
        "Scavenger Hunt",
        "Outdoor fitness class",
        "Community Service",
        "Minigolf / Golfing",
        "Camping",
    ]
    sh_ops = [
        "Clue",
        "Host a Dinner",
        "Bubble Bath",
        "Fire Pit",
        "Massages",
        "Video Game",
        "Something new for dinner",
        "Puzzle",
        "Meditate",
        "Candle Lit Dinner",
    ]
    pref_ops = ["Entertainment", "Dining", "Out Doors", "Stay At Home"]

    user_number_to_create_dates_for = 1

    def create_user(self):
        '''creates a user using the mimesis package'''
        person = {
            'username': generic.person.username(),
            'password': generic.person.password(),
            'full_name': generic.person.full_name(),
            'email': generic.person.email(),
            'location': address.city(),
        }
        return person
    

    def send_date(self):
        random_id2 = random.randint(2,25)
        user1 = User.objects.get(id=self.user_number_to_create_dates_for)
        user2 = User.objects.get(id=random_id2)
        date = {
            'random_user1': user1,
            'random_user2': user2,
            'location': address.city(),
            'when': d_time.datetime(2021, 2021)
        }
        return date

    
    def recieve_date(self):
        random_id1 = random.randint(2,25)
        user1 = User.objects.get(id=random_id1)
        user2 = User.objects.get(id=self.user_number_to_create_dates_for)
        date = {
            'random_user1': user1,
            'random_user2': user2,
            'location': address.city(),
            'when': d_time.datetime(2021, 2021)
        }
        return date


    def handle(self, *args, **options):
        if len(Entertainment.objects.all()) < 1:
            for option in self.e_ops:
                new_entertainment = Entertainment.objects.create(choice=option)

            for option in self.d_ops:
                new_Dining = Dining.objects.create(choice=option)

            for option in self.o_ops:
                new_outdoor = OutDoors.objects.create(choice=option)

            for option in self.sh_ops:
                new_stay_home = StayHome.objects.create(choice=option)

            for option in self.pref_ops:
                new_preferences = Preferences.objects.create(choice=option)
   
        if len(User.objects.all()) < 25:
            for _ in range(0,25):
                person = self.create_user()
                new_person = User.objects.create(
                    username=person['username'],
                    password=person['password'],
                    full_name=person['full_name'],
                    email=person['email'],
                    location=person['location']
                )

        if len(User.objects.all()) > 25:
            for _ in range(0,10):
                # notified_receiver = False
                random_date = random.randint(0,3)
                # random_amt_of_choices = random.randint(0,9)
                if _ % 2:
                    date = self.recieve_date()
                    # notified_receiver = True
                else:
                    date = self.send_date()
                new_date = DatesNightModel.objects.create(
                    users_one=date['random_user1'],
                    users_two=date['random_user2'],
                    location=date['location'],
                    when_date_time=date['when'],
                )
                if random_date == 0:
                    # random_choices = sorted(random.sample(range(0,9), random_amt_of_choices))
                    new_date.entertainment_category.set([1,3,5,6])
                elif random_date == 1:
                    new_date.dining_category.set([1,3,5,6])
                elif random_date == 2:
                    new_date.out_doors_category.set([1,3,5,6])
                else:
                    new_date.stay_home_category.set([1,3,5,6])
                # if notified_receiver:
                new_notification = Notification.objects.create(
                    date_night=new_date,
                    sent_user=date['random_user1'],
                    received_user=date["random_user2"],
                    # notified_received_user=notified_receiver,
                )
                # else:
                #     new_notification = Notification.objects.create(
                #         date_night=new_date,
                #         sent_user=date['random_user1'],
                #         received_user=date["random_user2"],
                #     )
            

        self.stdout.write(self.style.SUCCESS("Successfully added Preferences"))
