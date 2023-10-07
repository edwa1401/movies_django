# Generated by Django 4.2.5 on 2023-10-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 'Terrible'), (2, 'Bad'), (3, 'Satisfactory'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
