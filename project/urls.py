from django.urls import path

from project.views import project_items_update_view, project_update_view, project_item_delete_view, project_delete_view, \
    ProjectView, ProjectItemsView

app_name = 'project'
urlpatterns = [
    path('projectItemUpdate/', project_items_update_view, name='projectItemUpdate'),
    path('projectUpdate/', project_update_view, name='projectUpdate'),
    path('projectItemDelete/', project_item_delete_view, name='projectItemDelete'),
    path('projectDelete/', project_delete_view, name='projectDelete'),
    path('projectCreate/', ProjectView.as_view(), name='projectCreate'),
    path('projectItemsCreate/', ProjectItemsView.as_view(), name='projectItemsCreate'),

]
