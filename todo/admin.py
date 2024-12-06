from django.contrib import admin

from .models import TodoModel, VaccinationTodoModel
# Register your models here.
admin.site.register(TodoModel)
admin.site.register(VaccinationTodoModel)
