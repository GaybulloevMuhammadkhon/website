from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    content = models.TextField(blank=True,verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фото',blank=True)
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
    is_published = models.BooleanField(default=True,verbose_name='Публикация')
    cat = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,verbose_name='Категория')
    def __str__(self):
        return self.title

    #маршрут к конкретной записи
    def get_absolute_url(self):
        return reverse('post',kwargs ={'post_id':self.pk})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural= 'News'
        ordering = ['-time_create','title']


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True,verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'