from django.db import models


class Blog_Post(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', null=True, blank=True)
    views_count = models.BigIntegerField(default=0, verbose_name='Количество просмотров')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
