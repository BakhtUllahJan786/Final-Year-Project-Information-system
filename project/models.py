
from django.db import models
from django.forms import BooleanField
from student.models import Student
from django.contrib.auth.models import User
import requests
from student.models import Batch
class Project(models.Model):
    group_no=models.CharField(max_length=50)
    batch_no=models.ForeignKey(Batch,null=True,on_delete=models.CASCADE)
    student_1=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student1")
    student_2=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student2',null=True,blank=True)
    student_3=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student3',null=True,blank=True)
    superviser=models.ForeignKey(User,on_delete=models.CASCADE)
    project_title=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
    created_at = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.group_no
