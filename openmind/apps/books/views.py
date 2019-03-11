import json
import logging
from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Value, CharField, IntegerField
from django.utils import timezone
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from apps.core.utils import validate_data
from django.views.generic import FormView, TemplateView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from apps.core.exceptions import (
    HTTP404NotFoundError, HTTP400BadRequestError, HTTP403ForbiddenError)
from apps.books import models as book_models
from apps.books import serializers as book_sers
from apps.books.models import Book


# Create your views here.

class index(TemplateView):

    template_name = 'books/book.html'


class GetListBookAPI(APIView):
    def get(self, request, format=None):
        valid_data = validate_data(book_sers.GetListValidator, request.query_params)

        books = book_models.Book.objects.all().values()
        page_size = valid_data.get('page_size')
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paged_books = paginator.paginate_queryset(books, request)

        serializer = book_sers.BookSerializer(paged_books, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetDetailBook(APIView):
    def get(self, request, book_id):
        try:
            book = book_models.Book.objects.get(id=book_id).__dict__
        except ObjectDoesNotExist:
            raise HTTP404NotFoundError('Book not Found: {}'.format(book_id))

        serializer = book_sers.BookDetailSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetListBookRating(APIView):
    pass


class GetListBookSuggestion(APIView):
    pass


class GetListCollection(APIView):
    def get(self, request, format=None):
        valid_data = validate_data(book_sers.GetListValidator, request.query_params)

        collections = book_models.Collection.objects.all().values()
        page_size = valid_data.get('page_size')
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paged_collections = paginator.paginate_queryset(collections, request)

        serializer = book_sers.CollectionSerializer(paged_collections, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetListQuote(APIView):
    def get(self, request, format=None):
        valid_data = validate_data(book_sers.GetListValidator, request.query_params)

        quotes = book_models.Quote.objects.all().values()
        page_size = valid_data.get('page_size')
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paged_quotes = paginator.paginate_queryset(quotes, request)

        serializer = book_sers.CollectionSerializer(paged_quotes, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetListAuthor(APIView):
    def get(self, request, format=None):
        valid_data = validate_data(book_sers.GetListValidator, request.query_params)

        authors = book_models.Author.objects.all().values()
        page_size = valid_data.get('page_size')
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paged_authors = paginator.paginate_queryset(authors, request)

        serializer = book_sers.CollectionSerializer(paged_authors, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetListStory(APIView):
    def get(self, request, format=None):
        valid_data = validate_data(book_sers.GetListValidator, request.query_params)

        stories = book_models.Story.objects.all().values()
        page_size = valid_data.get('page_size')
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paged_stories = paginator.paginate_queryset(stories, request)

        serializer = book_sers.CollectionSerializer(paged_stories, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetListEvents(APIView):
    def get(self, request, format=None):
        valid_data = validate_data(book_sers.GetListValidator, request.query_params)

        events = book_models.Event.objects.all().values()
        page_size = valid_data.get('page_size')
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paged_events = paginator.paginate_queryset(events, request)

        serializer = book_sers.CollectionSerializer(paged_events, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetListNewBook(APIView):
    pass




