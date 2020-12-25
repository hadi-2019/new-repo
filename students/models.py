from django.db import models
from django.utils import timezone
from django.urls import reverse


class Student(models.Model):
    SEMESTER = [
        ('', 'choose...'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    ]
    GENDER = [
        ('male', 'male'),
        ('famale', 'famale')
    ]
    std_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='male')
    province = models.CharField(max_length=200)
    national_id = models.CharField(max_length=100, unique=True)
    current_address = models.CharField(max_length=500)
    hostel = models.BooleanField(default=False)
    budget = models.BooleanField(default=False)
    semester = models.CharField(max_length=10, choices=SEMESTER, default='1')
    image = models.ImageField(
        blank=True, upload_to="students/", default='default.jpg')

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})


class UploadFile(models.Model):
    upload_date = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/files")
