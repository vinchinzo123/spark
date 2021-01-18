# Generated by Django 3.1.5 on 2021-01-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notification_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notified_received_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='notified_sent_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('Sent', 'Sent'), ('Confirmed', 'Confirmed'), ('Declined', 'Declined'), ('No Match', 'No Match'), ('Cancelled', 'Cancelled')], default='Sent', max_length=10),
        ),
    ]
