from django.contrib import admin
from .models import TodoList, ListItem

# Register your models here.
admin.site.register(TodoList)
admin.site.register(ListItem)
