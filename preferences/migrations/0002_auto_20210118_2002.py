# Generated by Django 3.1.5 on 2021-01-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='choice',
            field=models.CharField(choices=[('Entertainment', 'Entertainment'), ('Dining', 'Dining'), ('Outdoors', 'Outdoors'), ('Stay Home', 'Stay Home')], max_length=50),
        ),
    ]