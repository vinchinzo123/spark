# Generated by Django 3.1.5 on 2021-01-14 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dates', '0003_auto_20210114_0104'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Sent', 'Sent'), ('Confirmed', 'Confirmed'), ('Declined', 'Declined'), ('No Match', 'No Match')], default='Sent', max_length=10)),
                ('date_night', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dates.datesnightmodel')),
                ('received_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_user', to=settings.AUTH_USER_MODEL)),
                ('sent_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
