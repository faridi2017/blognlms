from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Books(models.Model):
    barcode = models.CharField(max_length=13, primary_key=True)
    title=models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    published_year = models.SmallIntegerField()
    publication = models.CharField(max_length=60)
    is_issue = models.CharField(max_length=1,choices =(('Y','Yes'),('N','No')), default='N')
    mrp = models.SmallIntegerField()


    class Meta:
        managed = True
        db_table = 'Books'
        verbose_name_plural = "Books"


class Students(models.Model):
    enrollment_no = models.CharField(max_length=10, unique=True, primary_key=True)
    student_name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    pin = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    is_passed = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')),default='N')
    is_hostler = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), default='N')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'),('O', 'Other')))
    course = models.CharField(max_length=200)
    course_type = models.CharField(max_length=1, choices=(('R', 'Regular'), ('D', 'Distance'), ('P', 'Part_Time')))
    department = models.CharField(max_length=200)
    course_duration = models.FloatField(null=False, blank=False)
    joined_on = models.DateTimeField(auto_now_add=True)
    passing_year = models.SmallIntegerField(null=True,blank=True)
    dob = models.CharField(max_length=15,help_text='dd/mm/yyyy')

    class Meta:
        managed = True
        db_table = 'Students'
        verbose_name_plural = "Students"

class Checkouts(models.Model):
    barcode = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='book_details', primary_key=True)
    student_eno = models.ForeignKey(Students,on_delete=models.CASCADE, related_name='book_issued')
    issued_on = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=datetime.now() + timedelta(days=30))

    class Meta:
        managed = True
        db_table = 'Checkouts'
        verbose_name_plural = "Checkouts"
