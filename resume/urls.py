from django.urls import path

from resume.views import resume_update_view, resume_delete_view, UserResumeCreate

app_name = 'resume'
urlpatterns = [

    path('resumeUpdate/', resume_update_view, name='resumeUpdate'),
    path('resumeDelete/', resume_delete_view, name='resumeDelete'),
    path('resumeCreate/', UserResumeCreate.as_view(), name='resumeCreate'),

]
