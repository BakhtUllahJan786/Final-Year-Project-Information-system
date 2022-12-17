from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from project.views import project
from .forms import BatchForm,StudentForm
from django.contrib import messages
from django.core.paginator import Paginator
import csv,io
from .filters import StudentFilter
from project.models import Project

from .models import Student
from django.http import HttpResponse
import io


# Create your views here.
import csv
from django.http import HttpResponse

def exportFile(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Name', 'Roll No','Batch NO', 'Section', 'Project Status','Gender','Dues','Remarks'])
    
    for student in Student.objects.all().values_list('name','roll_number','batch_no','section','projet_status','gender','dues','remarks'):
        writer.writerow(student)
    response['Content-Disposition'] ='attachment; filename="student.csv"'
    return response

def home(request):
    return render(request,'home.html')

@login_required(login_url="login")
def Allstudent(request):
    project=Project.objects.all()
    student=Student.objects.all().order_by('-created_at')
    myfilter=StudentFilter(request.GET,queryset=student)
    student=myfilter.qs
    paginator=Paginator(student,8)
    page=request.GET.get('page')
    student=paginator.get_page(page)
    context = {'student': student,'myfilter':myfilter,'project':project}
    return render(request,'list.html', context)

@login_required(login_url="login")
def add_batch(request):
    form=BatchForm()
    if request.method == "POST":  
        form=BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singlestudent')
    else:
        form:BatchForm()
        
    return render(request,'add_batch.html',{'form':form})    


def addStudents(request):
    return render(request,'add_student.html')

def SingleStudent(request):
    form=StudentForm()
    if request.method == "POST":  
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Added Successfully')
            return redirect('singlestudent')
    else:
        form:StudentForm()
    
    return render(request,'singleStudent.html',{'form':form})


def update(request,id):
    
    data=Student.objects.get(pk=id)
    form=StudentForm(instance=data)
    
    if request.method=='POST':
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('list')
        
    return render(request,'singleStudent.html',{'form':form})

    
    
    

def delete(request,student_id):
    st=Student.objects.get(id=student_id)
    st.delete()
    return redirect('list')

