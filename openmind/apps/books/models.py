from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField()
    avatar = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'author'


class Publisher(models.Model):
    name = models.TextField()
    desc = models.TextField()
    avatar = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'publisher'


class BookSet(models.Model):
    title = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField(default='', blank=True)
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book_set'


class Collection(models.Model):
    title = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField(default='', blank=True)
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'collection'


class Category(models.Model):
    title = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField(default='', blank=True)
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'


class Book(models.Model):
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField(default='')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=128)
    tags = models.TextField()
    content = models.TextField()
    publisher = models.TextField()
    publisher_photo = models.TextField(null=True, default=None)
    year_published = models.DateField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book


class MediaFile(models.Model):
    AUDIO = 'audio'
    IMAGE = 'image'
    VIDEO = 'video'
    FILE_TYPE_CHOICES = (
        (IMAGE, 'Image'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    )

    name = models.CharField(max_length=300)
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'media_file'


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_category'

