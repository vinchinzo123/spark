# Generated by Django 3.1.5 on 2021-01-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='entertainment',
        ),
        migrations.AddField(
            model_name='preferences',
            name='entertainment_choices',
            field=models.CharField(choices=[('Netflix', 'Netflix'), ('Movies', 'Movies'), ('Concert', 'Concert'), ('Local Bar', 'Local Bar')], default='Netflix', max_length=15),
        ),
    ]
