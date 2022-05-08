from django.contrib.postgres import fields
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    content = models.TextField(blank=True)
    tags = fields.ArrayField(models.CharField(max_length=20), blank=True)

    published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return f"{self.id} {self.title}"
