# Generated by Django 3.1.4 on 2020-12-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20201221_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('', 'choose...'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=10),
        ),
    ]
