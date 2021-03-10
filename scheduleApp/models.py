from django.db import models

# Create your models here.
class Timing(models.Model):
    id = models.AutoField(primary_key=True)
    timing1 = models.TimeField(null=True, blank=True)
    timing2 = models.TimeField(null=True, blank=True)
    user = models.CharField(max_length=50,blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)


class Doctors(models.Model):
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50,null=True)
    number = models.CharField(max_length=50, null=True)
    timings = models.CharField(null=True,blank=True,max_length=180)


class Patient(models.Model):
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    # gender = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=50, null=True)