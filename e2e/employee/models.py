# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class UserMaster(models.Model):
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    otp = models.IntegerField( null=True)
    role = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=False, null=True)
    is_verified = models.BooleanField(default=False, null=True)
    is_created = models.DateTimeField(auto_now_add=True, null=True)
    is_updated = models.DateTimeField(auto_now_add=True, null=True)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=150, null=True)
    postalcode = models.CharField(max_length=50, null=True)
    dob = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    joblocation = models.CharField(max_length=150, null=True)
    jobregion = models.CharField(max_length=150, null=True)
    jobtype = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(upload_to="app/candidate/img", null=True)
    resume = models.FileField(upload_to="app/candidate/resume", null=True)

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=150, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=150, null=True)
    logo_pic = models.ImageField(upload_to="app/img/company", null=True)

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,default="", null=True)
    jobname = models.CharField(max_length=250, null=True)
    companyname = models.CharField(max_length=250, null=True)
    companyaddress = models.CharField(max_length=250, null=True)
    jobdescription = models.CharField(max_length=500, null=True)
    qualification = models.CharField(max_length=250, null=True)
    responsibilties = models.CharField(max_length=250, null=True)
    location = models.CharField(max_length=250, null=True)
    companywebsite = models.CharField(max_length=250, null=True)
    companyemail = models.CharField(max_length=250, null=True)
    companycontact = models.CharField(max_length=20, null=True)
    salarypackage = models.CharField(max_length=250, null=True)
    experience = models.CharField(max_length=10, null=True)
    jobtype=models.CharField(max_length=50, null=True)
    logo = models.ImageField(upload_to="app/img/jobpost", default="", null=True)

class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE, null=True)
    education = models.CharField(max_length=200, null=True)
    experience = models.IntegerField(default=0, null=True)
    website = models.CharField(max_length=200, null=True)
    min_salary = models.CharField(max_length=200, null=True)
    max_salary = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    resume = models.FileField(upload_to="app/resume", null=True)




