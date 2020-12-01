from django.contrib import admin
# Register your models here.

from django_todo_app.models import Tasks

admin.site.register(Tasks)