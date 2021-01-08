from django.db import models

# Create your models here.
class Entertainment(models.Model):
    '''
    '''
    E_CHOICES = [
        ('Netflix', 'Netflix'),
        ('Movies', 'Movies'),
        ('Concert', 'Concert'),
        ('Local Bar', 'Local Bar')
    ]
    entertainment_choices = models.CharField(max_length=15, choices=E_CHOICES)

    def __str__(self):
        return f'{self.entertainment_choices}'


class Dining(models.Model):
    D_CHOICES = [
        ('American', 'American'),
        ('Mexican', 'Mexican'),
        ('Jamican', 'Jamican'),
        ('Take out', 'Take out'),
        ('Desert', 'Desert'),
        ('Breakfast', 'Breakfast')
    ]
    dining_choices = models.CharField(max_length=50, choices=D_CHOICES)


    def __str__(self):
        return f'{self.dining_choices}'


class OutDoors(models.Model):
    # -outdoors FK (picnic, park,)
    O_CHOICES = [
        ('Picnic', 'Picnic'),
        ('Park', 'Park'),
        ('Hiking', 'Hiking'),
        ('Lake', 'Lake'),
        ('Swimming', 'Swimming'),
    ]
    outdoor_choices = models.CharField(max_length=50, choices=O_CHOICES)


    def __str__(self):
        return f'{self.outdoor_choices}'
    


class StayHome(models.Model):
    # -stay home FK (board games.. etc)
    SH_CHOICES = [
        ('Board Games', 'Board Games'),
    ]
    stay_home_choices = models.CharField(max_length=50, choices=SH_CHOICES)


    def __str__(self):
        return f'{self.stay_home_choices}'


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
        ('Entertainment', 'Entertainment'),
        ('Dining', 'Dining'),
        ('Outdoors', 'Outdoors'),
        ('Stay_Home', 'Stay_At_Home')
    ]
    choice = models.CharField(max_length=50, choices=P_CHOICES)
    def __str__(self):
        return f"{self.choice}"
