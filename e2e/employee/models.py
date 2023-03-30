# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activitylog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(db_column='Activity', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActivityLog'


class Application(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    jobid = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='JobID')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    applicationdate = models.DateField(db_column='ApplicationDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Application'


class Empavaliblity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    monday = models.IntegerField(db_column='Monday', blank=True, null=True)  # Field name made lowercase.
    tuesday = models.IntegerField(db_column='Tuesday', blank=True, null=True)  # Field name made lowercase.
    wednesday = models.IntegerField(db_column='Wednesday', blank=True, null=True)  # Field name made lowercase.
    thrusday = models.IntegerField(db_column='Thrusday', blank=True, null=True)  # Field name made lowercase.
    friday = models.IntegerField(db_column='Friday', blank=True, null=True)  # Field name made lowercase.
    saturday = models.IntegerField(db_column='Saturday', blank=True, null=True)  # Field name made lowercase.
    sunday = models.IntegerField(db_column='Sunday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpAvaliblity'


class Employee(models.Model):
    empid = models.AutoField(db_column='EmpID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    addressl1 = models.TextField(db_column='AddressL1', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    addressl2 = models.TextField(db_column='AddressL2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee'


class Employer(models.Model):
    emprid = models.AutoField(db_column='EmprID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    addressl1 = models.TextField(db_column='AddressL1', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    addressl2 = models.TextField(db_column='AddressL2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employer'


class Jobs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    postdate = models.DateField(db_column='PostDate')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salary = models.CharField(db_column='Salary', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hoursrequired = models.IntegerField(db_column='HoursRequired')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employer, models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Jobs'


class Rolemaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleMaster'


class Userlog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime', blank=True, null=True)  # Field name made lowercase.
    logouttime = models.DateTimeField(db_column='LogoutTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserLog'


class Usermaster(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    roleid = models.ForeignKey(Rolemaster, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserMaster'
