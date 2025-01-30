from django.db import models
from core.models import IsPublishedModel
from django.contrib.auth import get_user_model

Max_length_of_CharField = 256
User = get_user_model()


class Location(IsPublishedModel):
    name = models.CharField(
        'Название места',
        max_length=Max_length_of_CharField
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(IsPublishedModel):
    title = models.CharField('Заголовок', max_length=Max_length_of_CharField)
    description = models.TextField('Описание', )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL; '
                  'разрешены символы латиницы, цифры, дефис '
                  'и подчёркивание.'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(IsPublishedModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория',
        help_text='Укажите категорию для публикации.'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    title = models.CharField('Заголовок', max_length=Max_length_of_CharField)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text='Если установить дату и время в'
        ' будущем — можно делать отложенные публикации.'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='locations',
        verbose_name='Местоположение',
        help_text='Укажите местоположение '
        'публикации.'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
