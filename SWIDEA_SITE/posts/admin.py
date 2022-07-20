from django.contrib import admin
from .models import Post, Devtool


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Devtool)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name"]

