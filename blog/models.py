from django.db import models


class Post(models.Model):
    post_text = models.TextField()
    post_title = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add = True)
    post_image = models.ImageField(upload_to='event_images/')
