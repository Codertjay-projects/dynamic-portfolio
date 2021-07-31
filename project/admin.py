from django.contrib import admin
from .models import ProjectItem, Project

# Register your models here.


admin.site.register(Project)
admin.site.register(ProjectItem)
