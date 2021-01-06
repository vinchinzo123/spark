from django.core.management.base import BaseCommand
from preferences.models import Entertainment, Dining, OutDoors, StayHome

class Command(BaseCommand):
    help = 'Adds Peference options to their respective tables'

    def handle(self, *args, **options):
        new_entertainment = Entertainment.objects.create(
            entertainment_choices='Netflix'
        )
        new_entertainment = Entertainment.objects.create(
            entertainment_choices='Movies'
        )
        new_entertainment = Entertainment.objects.create(
            entertainment_choices='Concert'
        )
        new_entertainment = Entertainment.objects.create(
            entertainment_choices='Local Bar'
        )

        new_Dining = Dining.objects.create(
            dining_choices='American'
        )
        new_Dining = Dining.objects.create(
            dining_choices='Mexican'
        )
        new_Dining = Dining.objects.create(
            dining_choices='Jamican'
        )
        new_Dining = Dining.objects.create(
            dining_choices='Desert'
        )
        new_Dining = Dining.objects.create(
            dining_choices='Breakfast'
        )

        new_outdoor = OutDoors.objects.create(
            outdoor_choices='Picnic'
        )
        new_outdoor = OutDoors.objects.create(
            outdoor_choices='Park'
        )
        new_outdoor = OutDoors.objects.create(
            outdoor_choices='Hiking'
        )
        new_outdoor = OutDoors.objects.create(
            outdoor_choices='Lake'
        )
        new_outdoor = OutDoors.objects.create(
            outdoor_choices='Swimming'
        )

        new_stay_home = StayHome.objects.create(
            stay_home_choices='Board Games'
        )
        # new_stay_home = StayHome.objects.create(
        #     stay_home_choices='Park'
        # )
        # new_stay_home = StayHome.objects.create(
        #     stay_home_choices='Hiking'
        # )
        # new_stay_home = StayHome.objects.create(
        #     stay_home_choices='Lake'
        # )
        # new_stay_home = StayHome.objects.create(
        #     stay_home_choices='Swimming'
        # )

        self.stdout.write(self.style.SUCCESS('Successfully added Preferences'))