from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('edit/<int:pk>',views.TaskEdit,name='task_edit'),
    path('add_task',views.add_task,name='add_task'),
    path('delete/<int:pk>',views.delete,name='task_delete'),
    
]