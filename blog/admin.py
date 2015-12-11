from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_date')
    list_filter = ('title',)
    ordering = ('-publication_date',)

admin.site.register(Blog,BlogAdmin)