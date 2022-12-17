from django.contrib import admin
from .models import Student,Batch
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll_number','batch_no','section','gender','projet_status']
    #search_fields=['name','gender','projet_status']
    list_display_links=['name','roll_number','batch_no',]
    list_filter=['batch_no','section','projet_status']
    #list_filter=['status']
    list_per_page: 10
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Batch)