from django.contrib.auth import admin
from django.contrib import @admin.register(Portfolio)
from .models import portfolio, project

@admin.register(project)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created_at', 'updated_at')
    search_fields = ('project__name', 'project__description')

@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'portfolio_title', 'get_project_name')
    search_fields = ('user__first_name', 'user__last_name', 'portfolio_title', 'portfolio_description')
    list_filter = ('project__created__at')

    def get_user_full_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def get_project_name(self, obj):
        return obj.project.name if obj.project else 'N/A'
    get_project_name.short_description = 'Portfolio'

