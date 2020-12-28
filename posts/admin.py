from django.contrib import admin
from .models import Post, Report

class PostAdmin(admin.ModelAdmin):
    list_display = ['user','content','created_at','count','hidden','date_hidden','deleted_by']




admin.site.register(Report)
admin.site.register(Post,PostAdmin)
