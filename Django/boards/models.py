from django.db import models

# 게시글


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField