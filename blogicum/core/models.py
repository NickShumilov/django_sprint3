from django.db import models


class IsPublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
