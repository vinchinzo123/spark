from django.db import models

# Create your models here.
class Entertainment(models.Model):
    """"""

    E_CHOICES = [
        ("Netflix", "Netflix"),
        ("Movie Theater", "Movie Theater"),
        ("Concert", "Concert"),
        ("Local Bar", "Local Bar"),
        ("Ballet", "Ballet"),
        ("Escape Room", "Escape Room"),
        ("Axe Throwing", "Axe Throwing"),
        ("Sports Game", "Sports Game"),
        ("Trivia Night", "Trivia Night"),
        ("Comedy House", "Comedy House"),
    ]
    choice = models.CharField(max_length=15, choices=E_CHOICES)

    def __str__(self):
        return f"{self.choice}"


class Dining(models.Model):
    D_CHOICES = [
        ("American Cusine", "American Cusine"),
        ("Mexican Cusine", "Mexican Cusine"),
        ("Local Cafe", "Local Cafe"),
        ("Diner", "Diner"),
        ("Italian Cusine", "Italian Cusine"),
        ("Steakhouse", "Steakhouse"),
        ("Brunch", "Brunch"),
        ("Desert", "Desert"),
        ("Street Food", "Street Food"),
        ("Thai Cusine", "Thai Cusine"),
    ]
    choice = models.CharField(max_length=50, choices=D_CHOICES)

    def __str__(self):
        return f"{self.choice}"


class OutDoors(models.Model):
    # -outdoors FK (picnic, park,)
    O_CHOICES = [
        ("Picnic", "Picnic"),
        ("Park", "Park"),
        ("Hiking", "Hiking"),
        ("Lake", "Lake"),
        ("Swimming", "Swimming"),
    ]
    choice = models.CharField(max_length=50, choices=O_CHOICES)

    def __str__(self):
        return f"{self.choice}"


class StayHome(models.Model):
    # -stay home FK (board games.. etc)
    SH_CHOICES = [
        ("Board Games", "Board Games"),
    ]
    choice = models.CharField(max_length=50, choices=SH_CHOICES)

    def __str__(self):
        return f"{self.choice}"


class Preferences(models.Model):
    # entertainment = models.ManyToManyField(Entertainment)
    # dining = models.ManyToManyField(Dining)
    # outdoors = models.ManyToManyField(OutDoors)
    # stay_home = models.ManyToManyField(StayHome)
    # choice field options enter, dining, outd, stayhome
    # then load view for entertainment
    # ideas for in the  view. On POST of this form,
    # then if/ elif (s) that call other forms&views
    # if new_preference == 'dining':
    # return HttpResponseRedirect(reverse('dining'))
    # inside of those views we would limit the form output based upon the
    # category picked
    P_CHOICES = [
        ("Entertainment", "Entertainment"),
        ("Dining", "Dining"),
        ("Outdoors", "Outdoors"),
        ("Stay Home", "Stay Home"),
    ]
    choice = models.CharField(max_length=50, choices=P_CHOICES)

    def __str__(self):
        return f"{self.choice}"
