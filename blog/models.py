from django.db import models


class Post(models.Model):
    post_text = models.TextField()
    post_title = models.CharField(max_length=100)
    post_date = models.DateField()
    post_image = models.ImageField(upload_to='event_images/')

    def get_summary(self):  # функция обрезки текста поста блога на странице блога
        return self.post_text[:70]

    def __str__(self):  # функция вставки заголовка как названия поста в админпанель
        return self.post_title
