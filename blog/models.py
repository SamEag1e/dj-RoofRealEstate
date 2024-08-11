from django.db import models


class Post(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    brief = models.TextField()
    full_text = models.TextField()
    image = models.ImageField(upload_to="blog_images/")

    def __str__(self):
        return self.title
