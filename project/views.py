from tokenize import group
from django.shortcuts import render,redirect
from .models import Project
from .forms import *
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
import csv
from django.http import HttpResponse

def exportProject(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Group No', 'Batch No','Student 1','Student 2', 'Student 3', 'Superviser','Pect Title',])
    
    for project in Project.objects.filter(superviser=request.user).values_list('group_no','batch_no','student_1','student_2','student_3','superviser','project_title'):
        writer.writerow(project)
    response['Content-Disposition'] ='attachment; filename="groups.csv"'
    return response


@login_required
def project(request):
    form= ProjectForm()
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, 'Group created Successfully')
          return redirect('profile')
    
    else:
        form=ProjectForm()
    return render(request,'project/project.html',{'form':form})






@login_required
def profile(request):
    groups=Project.objects.filter(superviser=request.user,completed=False)
    paginator=Paginator(groups,8)
    page=request.GET.get('page')
    groups=paginator.get_page(page)
    context = {
        'groups' : groups,

    }
    return render(request,'project/profile.html',context)


@login_required
def completed_project(request):
    groups=Project.objects.filter(superviser=request.user,completed=True)
    paginator=Paginator(groups,8)
    page=request.GET.get('page')
    groups=paginator.get_page(page)
    context = {
        'groups' : groups,

    }
    return render(request,'project/completed.html',context)




@login_required
def delete_project(request,project_id):
    st=Project.objects.get(id=project_id)
    st.delete()
    return redirect('profile')
@login_required
def all_project(request):
    groups=Project.objects.filter(completed=False)
    paginator=Paginator(groups,8)
    page=request.GET.get('page')
    groups=paginator.get_page(page)
    
    context={
        'groups' : groups
    }
    return render(request,'project/all_projects.html',context)

def updateProject(request,project_id):
    
    data=Project.objects.get(pk=project_id)
    form=ProjectForm(instance=data)
    
    if request.method=='POST':
        form=ProjectForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request,'project/project.html',{'form':form})
