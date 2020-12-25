import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Student, UploadFile


@receiver(post_save, sender=UploadFile)
def create_bulk_student(sender, created, instance, *args, **kwargs):
    if created:
        opened = StringIO(instance.csv_file.read().decode())
        reading = csv.DictReader(opened, delimiter=',')
        students = []
        for row in reading:
            if 'std_id' in row and row['std_id']:
                reg = row['std_id']
                first_name = row['first_name'] if 'first_name' in row and row['first_name'] else ''
                last_name = row['last_name'] if 'last_name' in row and row['last_name'] else ''
                father_name = row['father_name'] if 'father_name' in row and row['father_name'] else ''
                gender = (row['gender']).lower(
                ) if 'gender' in row and row['gender'] else ''
                email = row['email'] if 'email' in row and row['email'] else ''
                phone = row['phone'] if 'phone' in row and row['phone'] else ''
                province = row['province'] if 'province' in row and row['province'] else ''
                current_address = row['current_address'] if 'current_address' in row and row['current_address'] else ''
                national_id = row['national_id'] if 'national_id' in row and row['national_id'] else ''

                check = Student.objects.filter(
                    std_id=reg).exists()
                if not check:
                    students.append(
                        Student(
                            std_id=reg,
                            first_name=first_name,
                            last_name=last_name,
                            father_name=father_name,
                            gender=gender,
                            email=email,
                            phone=phone,
                            province=province,
                            current_address=current_address,
                            national_id=national_id,
                        )
                    )

        Student.objects.bulk_create(students)
        instance.csv_file.close()
        instance.delete()


def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=UploadFile)
def delete_csv_file(sender, instance, *args, **kwargs):
    if instance.csv_file:
        _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Student)
def delete_image_on_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)
