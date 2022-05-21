from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.core.models import TimeStampModel


class Category(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"


class Post(TimeStampModel):
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL, related_name="category")
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    tags = ArrayField(models.CharField(max_length=20), blank=True, default=[])
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return f"{self.id}. {self.title}"
