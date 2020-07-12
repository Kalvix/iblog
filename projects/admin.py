from django.contrib import admin

# Register your models here.
from .models import Project, ProjectCategory


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title','description','technology',)
	search_fields = ('technology',)
	list_filter = ('category',)
	# fields = ('title','category',)

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

	