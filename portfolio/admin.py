from django.contrib import admin
from .models import Portfolio, Project

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['__str__']  # Optional: customize fields shown

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name']

# Register your models here.
