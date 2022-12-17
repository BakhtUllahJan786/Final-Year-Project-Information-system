from django import forms
from django.forms import ModelForm 
from .models import  Batch,Student

class DateInput(forms.DateInput):
    input_type='date'

class BatchForm(ModelForm):  
    class Meta:  
        model = Batch  
        widgets={'DateOfAdmission':DateInput(),
                'batch' : forms.NumberInput(attrs={'class' : 'form-control'}),
}
        fields = ['batch','DateOfAdmission']  
        
        labels={
            'batch':'Batch Number',
            'DateOfAdmission':'Date of Addmission'
        }
        
        
class StudentForm(ModelForm):  
    class Meta:  
        model = Student  
        fields = '__all__' 
        
        labels={
            'name':'Name',
            'batch_no':'Batch Number',
            'roll_no':'Roll No',
            'section':'Section',
            'projet_status':'Project Status',
            'gender':'Gender,',
            'dues':'Dues',
            'remarks':'Remarks'
        
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'batch_no' : forms.Select(attrs={'class' : 'form-control'}),
            'roll_no' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'section' : forms.Select(attrs={'class' : 'form-control'}),
            'projet_status' : forms.Select(attrs={'class' : 'form-control'}),
            'gender' : forms.Select(attrs={'class' : 'form-control'}),
            'dues' : forms.CheckboxInput(attrs={'class' : 'form-check-input','type':"checkbox",'style':'width: 30px; height: 30px;'}),
            'remarks' : forms.TextInput(attrs={'class' : 'form-control'}),


        }
        
        
    

