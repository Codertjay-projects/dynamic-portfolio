from django.contrib import admin
from .models import ProjectItem, Project, Skills, Testimonial, Service, Resume

# Register your models here.


admin.site.register(Project)
admin.site.register(ProjectItem)
admin.site.register(Skills)
admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(Resume)
