#Admin
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "FYP Admin"
admin.site.site_title = "FYP Managment Portal"
admin.site.index_title = "Welcome to FYP Managment Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('student.urls')),
    path('projects/',include('project.urls')),

    path('login/',include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
