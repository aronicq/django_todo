from django.urls import path, include
from django_todo_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TasksView, basename='Task')

urlpatterns = [
    path('', include(router.urls)),

]

# app_name = 'django_todo_app'