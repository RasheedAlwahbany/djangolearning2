import os

from core.db_functions import myFunc
# to run this file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wail_tut.settings')
# to run django config
import django
django.setup()
from django.db.models.functions import Concat
from django.db.models import F,Value
from django.db import models

from core.models import Student,Course,StudentDetail
# Course.objects.create(name="Python",description="Python Course")
# course=Course.objects.filter(id=1)
# print(course[0].description)

# obj=Course.objects.annotate(compind=Concat(F('course__name'),Value('-'),F('description'),Output_field=models.CharField()),a=myFunc(F('id')))
obj=Course.objects.annotate(compind=Concat(F('name'),Value('-'),F('description'),output_field=models.CharField()),a=myFunc(F('id')))
print(obj.values())
