# Generated by Django 3.1.5 on 2021-01-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
