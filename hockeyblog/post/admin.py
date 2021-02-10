from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content", "cups", "team_name"]
    prepopulated_fields = {"slug": ("title", "team_name", "cups",)}
    summernote_fields = ("content",)
   


admin.site.register(Post, PostAdmin)
