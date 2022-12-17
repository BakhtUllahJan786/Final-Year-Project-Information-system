from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm 
from .models import  Project



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        
        labels = {
            'Group No':'group_no',
            'Batch_No':'batch_no',
            'Student 1' : 'student_1',
            'Student 2' : 'student_2',
            'Student 3' : 'student_3',
            'Superviser' : 'superviser',
            'Project Title' : 'project_title',
            'completed':'Completed'
            
        }
        
        widgets = {
            'group_no' : forms.TextInput(attrs={'class' : 'form-control'}),
            'batch_no' : forms.Select(attrs={'class' : 'form-control'}),
            'student_1' : forms.Select(attrs={'class' : 'form-control'}),
            'student_2' : forms.Select(attrs={'class' : 'form-control'}),
            'student_3' : forms.Select(attrs={'class' : 'form-control'}),
            'superviser' : forms.Select(attrs={'class' : 'form-control'}),
            'project_title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'completed' : forms.CheckboxInput(attrs={'class' : 'form-check-input','type':"checkbox",'style':'width: 30px; height: 30px;'}),


        }