from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name=_("اسم الكورس"))
    description = models.TextField(max_length=1000,verbose_name=_("وصف الكورس"))
    
    
    
class Student(models.Model):
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    name = models.CharField(max_length=255,verbose_name=_("اسم الطالب"))
    
   
class StudentDetail(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    email = models.EmailField(max_length=255,verbose_name=_("البريد الالكتروني"))
    phone = models.CharField(max_length=255,verbose_name=_("رقم الهاتف"))
    address = models.TextField(max_length=1000,verbose_name=_("العنوان"))
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=_("الكورس"))    