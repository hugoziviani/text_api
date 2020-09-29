from django.db import models


class Text(models.Model):
    text_id = models.AutoField(primary_key=True)
    text = models.TextField(unique=True)
    inserted_at = models.DateTimeField(auto_now_add=True)

class Word(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(unique=True, max_length=100)
    inserted_at = models.DateTimeField(auto_now_add=True)