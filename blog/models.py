from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=300)
    post_title = models.CharField(max_length=100)
    post_date = models.DateTimeField()
    post_image = models.ImageField(upload_to='post_images/')
