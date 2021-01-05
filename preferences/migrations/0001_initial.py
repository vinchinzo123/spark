# Generated by Django 3.1.5 on 2021-01-05 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dining_choices', models.CharField(choices=[('American', 'American'), ('Mexican', 'Mexican'), ('Jamican', 'Jamican'), ('Take out', 'Take out'), ('Desert', 'Desert'), ('Breakfast', 'Breakfast')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entertainment_choices', models.CharField(choices=[('Netflix', 'Netflix'), ('Movies', 'Movies'), ('Concert', 'Concert'), ('Local Bar', 'Local Bar')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='OutDoors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdoor_choices', models.CharField(choices=[('Picnic', 'Picnic'), ('Park', 'Park'), ('Hiking', 'Hiking'), ('Lake', 'Lake'), ('Swimming', 'Swimming')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StayHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stay_home_choices', models.CharField(choices=[('Board Games', 'Board Games')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dining', models.ManyToManyField(to='preferences.Dining')),
                ('entertainment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preferences.entertainment')),
                ('outdoors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preferences.outdoors')),
                ('stay_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preferences.stayhome')),
            ],
        ),
    ]
