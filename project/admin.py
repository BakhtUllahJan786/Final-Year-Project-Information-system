import imp
from django.contrib import admin
from .models import *
# Register your models here.
    
class ProjectAdmin(admin.ModelAdmin):
    list_display=['group_no','batch_no','student_1','student_2','student_3','superviser','project_title','completed']
    #search_fields=['group_no','student_1','student_2','superviser','project_title']
    list_display_links  =['group_no','student_1','student_2']
    list_filter=['superviser','batch_no','completed']
    list_select_related=['superviser']
    #autocomplete_fields=['superviser']
admin.site.register(Project,ProjectAdmin)