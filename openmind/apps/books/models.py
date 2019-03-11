from django.db import models

# Create your models here.


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


class Author(models.Model):
    author_name = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField()
    cover_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'author'
        ordering = ['created_at']


class Publisher(models.Model):
    publisher_name = models.TextField()
    desc = models.TextField()
    cover_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'publisher'
        ordering = ['created_at']


class BookSet(models.Model):
    set_title = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField(default='', blank=True)
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book_set'
        ordering = ['created_at']


class Collection(models.Model):
    collection_title = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField(default='', blank=True)
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'collection'
        ordering = ['created_at']


class Category(models.Model):
    category_title = models.TextField()
    tags = models.TextField(default='', blank=True)
    desc = models.TextField(default='', blank=True)
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'


class YearPublished(models.Model):
    year = models.IntegerField()
    tags = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'year'


class Book(models.Model):
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    book_title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField()
    content = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    year_published = models.ForeignKey(YearPublished, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    image_file = models.TextField()
    audio_file = models.TextField()
    video_file = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'
        ordering = ['created_at']


class Story(models.Model):
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    story_title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField()
    content = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    year_published = models.ForeignKey(YearPublished, on_delete=models.CASCADE)
    book_related = models.ForeignKey(Book, on_delete=models.CASCADE)
    image_file = models.TextField()
    audio_file = models.TextField()
    video_file = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'story'
        ordering = ['created_at']


class Quote(models.Model):
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    quote_title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField()
    content = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book_related = models.ForeignKey(Book, on_delete=models.CASCADE)
    image_file = models.TextField()
    audio_file = models.TextField()
    video_file = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'quotes'
        ordering = ['created_at']


class Event(models.Model):
    cover_photo = models.TextField()
    thumbnail_photo = models.TextField()
    event_name = models.CharField(max_length=200)
    tags = models.TextField()
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    address = models.TextField()
    book_related = models.ForeignKey(Book, on_delete=models.CASCADE)
    image_file = models.TextField()
    audio_file = models.TextField()
    video_file = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'event'
        ordering = ['created_at']


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_category'

