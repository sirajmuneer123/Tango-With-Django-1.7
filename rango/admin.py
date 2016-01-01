from django.contrib import admin

# Register your models here.
from rango.models import Category, Page
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
class PageAdmin(admin.ModelAdmin):
	list_display = ['title','category','url']
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)