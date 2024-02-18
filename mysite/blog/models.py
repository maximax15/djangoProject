from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    pages = models.IntegerChoices("Pages", "1 2 3")
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return slugify(self.title)
