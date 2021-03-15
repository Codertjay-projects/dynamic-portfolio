from django.urls import path
from .views import (userDashboard,
                    UserProfileUpdate,
                    UserLayoutUpdate,
                    UserTestimonialCreate,
                    UserSkillCreate,
                    UserResumeCreate,
                    UserNameUpdate,
                    ProjectView,
                    ProjectItemsView,
                    skill_update_view,
                    testimonail_update_view,
                    services_update_view,
                    UserServiceCreate,
                    project_items_update_view,
                    project_item_delete_view,
                    project_delete_view,
                    project_update_view,
                    skill_delete_view,
                    testimonial_delete_view,
                    service_delete_view, resume_delete_view, resume_update_view)

app_name = 'dashboard'

urlpatterns = [
    path('', userDashboard, name='dashboard'),

    # the create part
    path('testimonialCreate/', UserTestimonialCreate.as_view(), name='testimonialCreate'),
    path('skillCreate/', UserSkillCreate.as_view(), name='skillCreate'),
    path('serviceCreate/', UserServiceCreate.as_view(), name='serviceCreate'),
    path('resumeCreate/', UserResumeCreate.as_view(), name='resumeCreate'),
    path('projectCreate/', ProjectView.as_view(), name='projectCreate'),
    path('projectItemsCreate/', ProjectItemsView.as_view(), name='projectItemsCreate'),

    # the update part and some create
    path('profileUpdate/', UserProfileUpdate.as_view(), name='profileUpdate'),
    path('userUpdate/', UserNameUpdate.as_view(), name='userUpdate'),
    path('layoutUpdate/', UserLayoutUpdate.as_view(), name='layoutUpdate'),

    # update only view
    path('skillUpdate/', skill_update_view, name='skillUpdate'),
    path('testimonialUpdate/', testimonail_update_view, name='testimonialUpdate'),
    path('serviceUpdate/', services_update_view, name='serviceUpdate'),
    path('projectItemUpdate/', project_items_update_view, name='projectItemUpdate'),
    path('projectUpdate/', project_update_view, name='projectUpdate'),
    path('resumeUpdate/', resume_update_view, name='resumeUpdate'),

    # delete only view
    path('projectItemDelete/', project_item_delete_view, name='projectItemDelete'),
    path('projectDelete/', project_delete_view, name='projectDelete'),
    path('testimonialDelete/', testimonial_delete_view, name='testimonialDelete'),
    path('skillDelete/', skill_delete_view, name='skillDelete'),
    path('serviceDelete/', service_delete_view, name='serviceDelete'),
    path('resumeDelete/', resume_delete_view, name='resumeDelete')
]
