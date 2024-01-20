from django.db import models
from news.validators import validate_min_two_words


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    role = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        validators=[validate_min_two_words],
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
