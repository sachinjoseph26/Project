# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    joblocation = models.CharField(max_length=150)
    jobregion = models.CharField(max_length=150)
    jobtype = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="app/candidate/img")
    resume = models.FileField(upload_to="app/candidate/resume")

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo_pic = models.ImageField(upload_to="app/img/company")

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,default="")
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.CharField(max_length=500)
    qualification = models.CharField(max_length=250)
    responsibilties = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=250)
    experience = models.CharField(max_length=10)
    jobtype=models.CharField(max_length=50)
    logo = models.ImageField(upload_to="app/img/jobpost", default="")

class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    education = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    website = models.CharField(max_length=200)
    min_salary = models.CharField(max_length=200)
    max_salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    resume = models.FileField(upload_to="app/resume")




