from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')


class News(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        validators=[validate_title])
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=False)

    def __str__(self):
        return self.title
