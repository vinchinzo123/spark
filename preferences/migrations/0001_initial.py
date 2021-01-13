# Generated by Django 3.1.5 on 2021-01-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('American Cusine', 'American Cusine'), ('Mexican Cusine', 'Mexican Cusine'), ('Local Cafe', 'Local Cafe'), ('Diner', 'Diner'), ('Italian Cusine', 'Italian Cusine'), ('Steakhouse', 'Steakhouse'), ('Brunch', 'Brunch'), ('Desert', 'Desert'), ('Street Food', 'Street Food'), ('Thai Cusine', 'Thai Cusine')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('Netflix', 'Netflix'), ('Movie Theater', 'Movie Theater'), ('Concert', 'Concert'), ('Local Bar', 'Local Bar'), ('Ballet', 'Ballet'), ('Escape Room', 'Escape Room'), ('Axe Throwing', 'Axe Throwing'), ('Sports Game', 'Sports Game'), ('Trivia Night', 'Trivia Night'), ('Comedy House', 'Comedy House')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='OutDoors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('Picnic', 'Picnic'), ('Park', 'Park'), ('Hiking', 'Hiking'), ('Lake', 'Lake'), ('Swimming', 'Swimming')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('Entertainment', 'Entertainment'), ('Dining', 'Dining'), ('Outdoors', 'Outdoors'), ('Stay_Home', 'Stay_At_Home')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StayHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('Board Games', 'Board Games')], max_length=50)),
            ],
        ),
    ]
