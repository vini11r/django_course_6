from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок блога")
    content = models.TextField(verbose_name="Содержание блога")
    images = models.ImageField(upload_to="blog/images", verbose_name="Превью блога", blank=True, null=True)
    publish_at = models.DateField(verbose_name="Дата публикации", blank=True, null=True)
    count_views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
