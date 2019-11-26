from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'age')

admin.site.register(Student, StudentAdmin)

# Register your models here.
