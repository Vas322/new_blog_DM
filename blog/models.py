from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Модель описывает пост"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
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


class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('Автор комментария', max_length=100)
    text = models.TextField('Тест комментария')
    created_date = models.DateTimeField('Дата создания поста', default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    class Meta:
        """Атрибут, позволяющий использовать форму множественного числа 'Комментарии' """
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def approve(self):
        """Метод, подтверждающий публикацию комментарий"""
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        """Метод возвращает строковое представление модели"""
        return self.text
