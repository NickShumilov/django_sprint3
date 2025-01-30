from django.contrib import admin
from .models import Location
from .models import Category
from .models import Post


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
    )
    search_fields = (
        'name',
        'created_at',
    )
    list_filter = (
        'name',
        'created_at',
    )
    list_display_links = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug'
    )
    list_editable = (
        'description',
        'slug'
    )
    search_fields = (
        'title',
        'description',
        'slug'
    )
    list_filter = (
        'title',
        'description',
        'slug'
    )
    list_display_links = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'author',
        'text',
        'pub_date',
        'location',
        'category'
    )
    list_editable = (
        'author',
        'text',
        'pub_date',
        'location',
        'category'
    )
    search_fields = (
        'title',
        'created_at',
        'author',
        'text',
        'pub_date',
        'location',
        'category'
    )
    list_filter = (
        'title',
        'created_at',
        'author',
        'text',
        'pub_date',
        'location',
        'category'
    )
    list_display_links = ('title',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
