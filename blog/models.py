from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_images")
    content = models.TextField()
    catagory = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_app:post_detail_view", kwargs={"pk": self.pk})
