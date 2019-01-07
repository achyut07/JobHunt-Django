from django.db import models
from django.contrib.auth.models import AbstractUser
import smtplib
CHOICES=[('Employeer','Employeer'),
         ('jobseeker','jobseeker')]
job=[('Full Time','Full Time'),
     ('Part Time','Part Time'),
     ('Intern','Intern')]

class User(AbstractUser):
    Department = models.CharField(max_length=500, blank=True)
    Contactnum = models.CharField(max_length=30, blank=True)
    Choose = models.CharField(max_length=17,choices=CHOICES)

class Company(models.Model):
    Companyname=models.CharField(max_length=100,blank=False,null=True)
    Location=models.CharField(max_length=100,blank=False,null=True)
    job_title=models.CharField(max_length=100,blank=False,null=True)
    job_description=models.TextField(max_length=500,blank=False,null=True)
    Image = models.ImageField(upload_to='mypics/%Y/%m/%d', default='../img/noimage.png', blank=True, null=True)
    Company_email=models.EmailField()
    JobNature=models.CharField(max_length=15,choices=job)
    Salary=models.CharField(max_length=100,blank=False,null=True)
    post_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return  self.job_title

class Jobsearch(models.Model):
    job_title=models.CharField(max_length=100,blank=False,null=True)

class Apply(models.Model):
    Applier_email=models.EmailField(max_length=100)
    Company_email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    cv=models.FileField()




    


