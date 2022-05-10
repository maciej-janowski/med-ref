from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from sqlalchemy import null
from .test_types import TEST_TYPE
from django.core.validators import MaxValueValidator,RegexValidator

# Create your models here.


class Patient(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=30, null=True)
    # pesel = models.IntegerField(null=False,blank=False,validators=[MaxValueValidator(99999999999)])
    pesel = models.CharField(null=False,blank=False,max_length=11)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=25,blank=False,null=False)
    street = models.CharField(max_length=50,blank=False,null=False)
    street_no = models.CharField(max_length=10)
    flat_no = models.CharField(max_length=10)
    # setting specific format for postal code
    postal_code = models.CharField(max_length=6,null=False,blank=False,validators=[RegexValidator(regex='^[0-9]{2}-[0-9]{3}',
    message='You must provide code in format DD-DDD')])
    sex = models.CharField(max_length=6,blank=False,null=False,choices=SEX)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Clinic(models.Model):
   name = models.CharField(max_length=30, null=False)
   city = models.CharField(max_length=25,blank=False,null=False)
   street = models.CharField(max_length=50,blank=False,null=False)
   street_no = models.CharField(max_length=10)
   postal_code = models.CharField(max_length=6,null=False,blank=False)
   
   def __str__(self):
       return f'{self.name}'

class Medic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    doc_number = models.IntegerField(validators=[MaxValueValidator(99999999999)],null=False,blank=False)
    clinic_info = models.ForeignKey(Clinic,null=True, on_delete=models.SET_NULL)

    def __str__(self):
       return f'{self.name} {self.last_name}'


class Test(models.Model):
    fk_patient = models.ForeignKey(Patient,null=False,on_delete=models.CASCADE)
    fk_medic = models.ForeignKey(Medic,null=False,on_delete=models.CASCADE)
    date_of_issue = models.DateField()

    def __str__(self):
       return f'Test {self.pk} for {self.fk_patient.name} {self.fk_patient.last_name} issued by {self.fk_medic.name} {self.fk_medic.last_name}'

class TestType(models.Model):

    item = models.ForeignKey(Test,null=True,on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50,blank=True,null=True,choices=TEST_TYPE)

    def __str__(self):
        return f'{self.test_type}'