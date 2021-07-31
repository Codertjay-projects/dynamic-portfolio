from django.urls import path

from skill.views import skill_delete_view, skill_update_view, UserSkillCreate

app_name = 'skill'
urlpatterns = [
    path('skillUpdate/', skill_update_view, name='skillUpdate'),
    path('skillCreate/', UserSkillCreate.as_view(), name='skillCreate'),
    path('skillDelete/', skill_delete_view, name='skillDelete'),

]
