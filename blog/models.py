from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Модель описывает пост"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название поста', max_length=200)
    text = models.TextField('Текст поста')
    created_date = models.DateTimeField('Дата создания поста', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации поста (опционно)', blank=True,
                                          null=True)

    created_date = models.DateTimeField('Дата создания поста', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации поста (опционно)', blank=True,
                                          null=True)

    class Meta:
        """Атрибут, позволяющий использовать форму множественного числа 'Посты' """
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def publish(self):
        """Метод публикации поста"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
