from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


