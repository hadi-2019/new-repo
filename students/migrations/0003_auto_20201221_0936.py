# Generated by Django 3.1.4 on 2020-12-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='students/'),
        ),
    ]
