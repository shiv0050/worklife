from django.urls import path
from . import views
urlpatterns = [
path('',views.home,name=""),
path('create-task',views.createTask,name='create-task'),
path('dashboard',views.dashboard,name="dashboard"),
path('view-task',views.viewTask,name='view-task'),
path('update-task/<str:pk>/',views.updateTask,name="update-task"),
path('complete-task/<str:pk>/',views.completeTask,name="complete-task")
]