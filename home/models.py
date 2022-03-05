from django.db import models
import datetime
from datetime import date
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone
from django.contrib.staticfiles import finders
# Create your models here.
class dept(models.Model):
    dname=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return str(self.dname)
class subDeptart(models.Model):
    Dname=models.ForeignKey(dept,on_delete=models.SET_NULL,null=True)
    subDname=models.CharField(max_length=50)
    def __str__(self):
        return str(self.subDname)
class employee(models.Model):
    #personal 
    ename=models.CharField(max_length=60)
    father_name=models.CharField(max_length=50,blank=True,null=True)
    FamilyNo=models.IntegerField(null=True)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100,null=True,blank=True)
    #job
    Designation=models.CharField(max_length=61)
    subDept=models.ForeignKey(subDeptart,on_delete=models.SET_NULL,null=True)
    #id card
    Cnic=models.IntegerField()
    issueDate=models.DateField(null=True)
    DateOfExpire=models.DateField(null=True)
    nicCopy=models.ImageField(upload_to='nicCopy',default='profile.JPEG')
    
    
    District=models.CharField(max_length=150,blank=True,null=True)
    Province=models.CharField(max_length=150,blank=True,null=True)
    Country=models.CharField(max_length=150,blank=True,null=True)
    
    
    
    Address=models.CharField(max_length=150,blank=True,null=True)
    pic=models.ImageField(upload_to='img',default='profile.JPEG')
    
    date=models.DateField(auto_now_add=True,blank=True,null=True)
    salery=models.IntegerField()
    resign=models.BooleanField(default=False)
    def __str__(self):
        return str(self.ename)
    import os
    def logo_dir_path(instance, filename):
        extension = pic.split('.')[-1]
        og_filename = pic.split('.')[0]
        new_filename = "shop_%s.%s" % (instance.name, extension)

        return new_filename
    @property
    def get_monthly_att(self):
        month=date.today().strftime('%Y-%m')
        
        mo=Attendance_month.objects.get(month=month)
        
        att=Attendance.objects.filter(months_attendance=mo,subd=self.subDept,emp=self.id).order_by('date')
        return att
    @property
    def get__history_monthly(self,hdate):
        month=hdate.strftime('%Y-%m')
        
        mo=Attendance_month.objects.get(month=month)
        
        att=Attendance.objects.filter(months_attendance=mo,subd=self.subDept,emp=self.id).order_by('date')
        return att
    @property
    def emp_count(self):
        month=date.today().strftime('%Y-%m')
        import datetime
        import calendar
        now = datetime.datetime.now()
        days=calendar.monthrange(now.year, now.month)[1]
        
        mo=Attendance_month.objects.get(month=month)
        
        att=Attendance.objects.filter(months_attendance=mo,subd=self.subDept,emp=self.id).count()
        list = []
        for i in range(0,days-att):
            list.append(i)
        return list
    @property
    def emp_present_count(self):
        month=date.today().strftime('%Y-%m')
        mo=Attendance_month.objects.get(month=month)
        att=Attendance.objects.filter(months_attendance=mo,subd=self.subDept,emp=self.id,status='P').count()
        
        return att
    @property
    def emp_Absent_count(self):
        month=date.today().strftime('%Y-%m')
        mo=Attendance_month.objects.get(month=month)
        att=Attendance.objects.filter(months_attendance=mo,subd=self.subDept,emp=self.id,status='A').count()
        return att
    @property
    def emp_Reset_count(self):
        month=date.today().strftime('%Y-%m')
        mo=Attendance_month.objects.get(month=month)
        att=Attendance.objects.filter(months_attendance=mo,subd=self.subDept,emp=self.id,status='R').count()
        return att
  
    
class Attendance_month(models.Model):
    month=models.CharField(max_length=50,null=True,blank=True,unique=True)
    def __str__(self):
        return str(self.month)
    
class Attendance(models.Model):
    ch=[
        ('P','P'),
        ('A','A'),
        ('R','R')
    ]
    
    emp=models.ForeignKey(employee,null=True,blank=True,on_delete=models.SET_NULL)
    months_attendance=models.ForeignKey(Attendance_month,null=True,on_delete=models.SET_NULL)
    subd=models.ForeignKey(subDeptart,on_delete=models.SET_NULL,null=True,)
    status=models.CharField(max_length=30,choices=ch,null=True,blank=True)
    date=models.DateField(null=True,blank=True,default=timezone.now)
    def __str__(self):
        return str(self.emp.ename+"__"+str(self.date))
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['emp', 'date'], name='unique_user_post'),
        ]
    