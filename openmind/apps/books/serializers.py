import json
from rest_framework import serializers
from django.conf import settings
from apps.books import models as books_models

# PUBLISH_ASC = 'publish-asc'
# PUBLISH_DESC = 'publish-desc'
# NAME_ASC = 'name-asc'
# NAME_DESC = 'name-desc'
# SELL_RANKING_ASC = 'sell-ranking-asc'
# SELL_RANKING_DESC = 'sell-ranking-desc'


class GetListValidator(serializers.Serializer):
    page = serializers.IntegerField(default=settings.DEFAULT_PAGE)
    page_size = serializers.IntegerField(default=settings.DEFAULT_PAGE_SIZE)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.Author
        fields = ('id', 'author_name', 'desc', 'avatar', 'created_at', 'updated_at')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.Publisher
        fields = ('id', 'publisher_name', 'desc', 'avatar', 'created_at', 'updated_at')


class BookSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.BookSet
        fields = (
            'id', 'set_title', 'cover_photo', 'thumbnail_photo', 'tags',
            'price', 'desc', 'created_at', 'updated_at'
        )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = books_models.Collection
        fields = (
            'id', 'collection_title', 'cover_photo', 'thumbnail_photo', 'tags',
            'price', 'desc', 'created_at', 'updated_at'
        )


class YearPublished(serializers.ModelSerializer):
    class Meta:
        model = books_models.YearPublished
        fields = (
            'id', 'year', 'tags', 'created_at', 'updated_at'
        )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = books_models.Book
        fields = (
            'id', 'cover_photo', 'thumbnail_photo', 'book_title',
            'desc', 'tags', 'price', 'content', 'authors',
            'publisher', 'year_published', 'image_file',
            'audio_file', 'video_file',
            'created_at', 'updated_at',
        )


class BookDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = books_models.Book
        fields = (
            'id', 'cover_photo', 'title', 'desc', 'tags', 'publisher',
            'publisher_desc', 'publisher_photo',
            'price', 'book_type', 'isbn_code', 'jan_code',
            'item_id_ios', 'item_id_android',
            'created_at', 'updated_at', 'book_indexes', 'authors',
            'is_buy', 'allow_trial'
        )


class StorySerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = books_models.Story
        fields = (
            'id', 'cover_photo', 'thumbnail_photo', 'story_title',
            'desc', 'tags', 'content', 'authors',
            'publisher', 'year_published', 'image_file',
            'audio_file', 'video_file',
            'created_at', 'updated_at',
        )


class GetListQuoteValidator(serializers.Serializer):
    page = serializers.IntegerField(default=settings.DEFAULT_PAGE)
    page_size = serializers.IntegerField(default=settings.DEFAULT_PAGE_SIZE)


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = books_models.Quote
        fields = (
            'id', 'cover_photo', 'thumbnail_photo', 'Quote_title',
            'desc', 'tags', 'content', 'authors', 'publisher',
            'image_file', 'audio_file', 'video_file',
            'created_at', 'updated_at',
        )
