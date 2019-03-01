from django.db import models

# Create your models here.


class Book(models.Model):
    cover_photo = models.TextField()
    book = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    tags = models.TextField()
    content = models.TextField()
    publisher = models.TextField()
    publisher_desc = models.TextField(null=True, default=None)
    publisher_photo = models.TextField(null=True, default=None)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book


class Author(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='authors')
    name = models.TextField()
    desc = models.TextField()
    avatar = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'author'


class Chapter(models.Model):
    book = models.CharField(max_length=200)
    chapter = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.chapter

