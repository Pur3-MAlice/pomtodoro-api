# Generated by Django 3.2.23 on 2023-11-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='last_completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
