from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import Post

"""
class PostInline(admin.TabularInline):
    model = Post
    extra = 3
"""


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Введите автора', {'fields': ['author']}),
        ('Введите название поста', {'fields': ['title']}),
        ('Введите текст поста', {'fields': ['text']}),
        ('Информация о дате создания поста', {'fields': ['created_date']}),
        ('Информация о дате публикации поста', {'fields': ['published_date']}),
    ]
    # inlines = [PostInline]
    list_display = ('title', 'created_date',
                    'published_date', 'author')  # список полей в таблице
    list_filter = ['created_date']  # боковая панель с фильтром по дате
    list_filter = ['author']  # боковая панель с фильтром по дате
    search_fields = ['title']  # добавляем поиск по свойству title


admin.site.register(Post, PostAdmin)
