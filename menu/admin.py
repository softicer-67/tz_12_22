from django.contrib import admin
from menu.models import MenuCategories


@admin.register(MenuCategories)
class MenuCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'url']
    search_fields = ['name', 'parent']
