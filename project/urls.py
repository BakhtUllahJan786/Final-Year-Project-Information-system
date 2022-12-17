from django.urls import path
from .import views
urlpatterns = [
    path('',views.project,name='project'),
    path('profile/',views.profile,name='profile'),
    path('completed-project/',views.completed_project,name='completed-project'),
    path('delete/<str:project_id>',views.delete_project,name='delete-project'),
    path('updateproject/<str:project_id>',views.updateProject,name='update-project'),
    path('allproject/',views.all_project,name='allproject'),
    path('exportProject/',views.exportProject,name='exportProject'),




    
]