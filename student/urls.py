from django.urls import path
from .import views
urlpatterns = [
    #path('',views.home,name='home'),
    path('',views.Allstudent,name='list'),
    path('add_batch/',views.add_batch,name='add-batch'),
    path('add_students/',views.addStudents,name='add-students'),
    path('singlestudent/',views.SingleStudent,name='singlestudent'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:student_id>',views.delete,name='delete'),
    path('export/',views.exportFile,name='export'),



    
]